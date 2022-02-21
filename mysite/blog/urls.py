from blog.views import (BlogListView, CreateBlogView, DeleteBlogView,
                        DetailBlogView, EditBlogView)
from django.urls import path

app_name = "blog"

urlpatterns = [
    path("list/", BlogListView.as_view(), name="list"),
    path("create/", CreateBlogView.as_view(), name="create"),
    path("<slug>/", DetailBlogView.as_view(), name="detail"),
    path("<slug>/edit/", EditBlogView.as_view(), name="edit"),
    path("<slug>/delete/", DeleteBlogView.as_view(), name="delete"),
]
