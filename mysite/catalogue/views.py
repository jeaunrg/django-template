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


class CatalogueView(ListView):
    model = Document
    paginate_by = 3
    template_name = 'catalogue/catalogue.html'
    ordering = ['-date_published']

    context_object_name = 'all_search_results'
    searchable_fields = ['titre', 'description', 'no_inventaire', 'categorie', 'theme',
                         'technique', 'support', 'region', 'lieu', 'epoque', 'type_collection',
                         'description']
    specifications = {field: "__icontains" for field in searchable_fields}

    def get_queryset(self):
        result = super(CatalogueView, self).get_queryset()
        filter_query = []
        for field in self.searchable_fields:
            value = self.request.GET.get(field)
            if value:
                filter_query.append(f"Q({field}{self.specifications.get(field)}='{value}')")
        print(filter_query)
        if filter_query:
            result = eval("Document.objects.filter(" + " | ".join(filter_query) + ")")
        else:
            result = Document.objects.all()

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_filter_bar'] = True
        context['searchable_fields'] = self.searchable_fields
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if request.FILES.get('catalogue'):
                for args in extract_catalogue(request.FILES['catalogue']):
                    args['author'] = request.user
                    object = Document(**args)
                    object.save()
            elif request.POST.get('delete_catalogue'):
                Document.objects.all().delete()
        return redirect('catalogue:list')


class DeleteDocumentView(LoginRequiredMixin, DeleteView):
    model = Document
    success_url = '/catalogue/list'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
