from django.urls import path

from .views import ContactView, download_data_view, generate_pdf_view

app_name = "personal"

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("pdf/<slug>/<download>/", generate_pdf_view, name="pdf"),
    path("data/<filter>/<query>/", download_data_view, name="data"),
]
