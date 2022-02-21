from django.urls import path
from .views import ContactView, download_data_view, generate_pdf_view


app_name = 'personal'

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("pdf/", generate_pdf_view, name="pdf"),
    path("data/", download_data_view, name="data"),
]
