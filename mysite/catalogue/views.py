from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from catalogue.models import Document
from catalogue.forms import DocumentForm
from account.models import Account
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .core import extract_catalogue
from django.contrib.auth.decorators import login_required
import django_filters
from django_filters.views import FilterView


class CreateDocumentView(LoginRequiredMixin, CreateView):
    form_class = DocumentForm
    template_name = 'catalogue/create_document.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = Account.objects.filter(username=self.request.user.username).first()
        self.object.save()
        return redirect('catalogue:list')


class EditDocumentView(LoginRequiredMixin, UpdateView):
    model = Document
    fields = ['titre', 'description', 'image']
    template_name = 'catalogue/edit_document.html'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user != object.author:
            return redirect('catalogue:detail', object.slug)
        return UpdateView.dispatch(self, request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))


class DetailDocumentView(DetailView):
    model = Document
    template_name = 'catalogue/detail_document.html'


class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = Document
        fields = ['titre', 'description', 'no_inventaire', 'categorie', 'theme',
                  'technique', 'support', 'region', 'lieu', 'epoque', 'type_collection',
                  'description']
        fields = {'titre': ['contains'],
                  'description': ['contains'],
        }


class CatalogueView(FilterView, ListView):
    model = Document
    context_object_name = 'document_list'
    template_name = 'catalogue/catalogue.html'
    filterset_class = DocumentFilter
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_filter_bar'] = True
        return context

#
# class CatalogueView(ListView):
#     model = Document
#     paginate_by = 20
#     template_name = 'catalogue/catalogue.html'
#     ordering = ['-date_published']
#     context_object_name = 'all_search_results'
#
#     def get_queryset(self):
#        result = super(CatalogueView, self).get_queryset()
#        query = self.request.GET.get('search')
#        if query:
#           postresult = Document.objects.filter(titre__contains=query)
#           result = postresult
#        else:
#            result = Document.objects.all()
#        return result



class DeleteDocumentView(LoginRequiredMixin, DeleteView):
    model = Document
    success_url = '/catalogue/list'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@login_required
def upload_view(request):
    if request.method == 'POST' and request.FILES['catalogue']:
        for args in extract_catalogue(request.FILES['catalogue']):
            args['author'] = request.user
            object = Document(**args)
            object.save()
        return redirect('catalogue:list')

    return render(request, 'catalogue/settings.html')
