from django.urls import path
from catalogue.views import (
    DetailDocumentView,
    CreateDocumentView,
    EditDocumentView,
    CatalogueView,
    DeleteDocumentView,
)

app_name = 'catalogue'

urlpatterns = [
    path('list/', CatalogueView.as_view(), name="list"),
    path('create/', CreateDocumentView.as_view(), name="create"),
    path('<slug>/', DetailDocumentView.as_view(), name="detail"),
    path('<slug>/edit/', EditDocumentView.as_view(), name="edit"),
    path('<slug>/delete/', DeleteDocumentView.as_view(), name="delete"),
]
