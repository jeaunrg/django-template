from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from blog.models import BlogPost
from blog.forms import BlogPostForm
from account.models import Account
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView


class CreateBlogView(LoginRequiredMixin, CreateView):
    form_class = BlogPostForm
    template_name = 'blog/create_blog.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = Account.objects.filter(username=self.request.user.username).first()
        self.object.save()
        return redirect('blog:list')


class EditBlogView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'body', 'image']
    template_name = 'blog/edit_blog.html'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if request.user != object.author:
            return redirect('blog:detail', object.slug)
        return UpdateView.dispatch(self, request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))


class DetailBlogView(LoginRequiredMixin, DetailView):
    model = BlogPost
    template_name = 'blog/detail_blog.html'


class BlogListView(LoginRequiredMixin, ListView):
    model = BlogPost
    paginate_by = 20
    template_name = 'blog/list_blog.html'
    ordering = ['-date_published']


class DeleteBlogView(DeleteView):
    model = BlogPost
    success_url = '/blog/list'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
