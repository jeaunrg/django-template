from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Account
import copy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from io import BytesIO
from django.http import HttpResponse
from .utils import generate_pdf

# nom du fichier de données téléchargé
EXCEL_FILENAME = "data.xlsx"
EXCEL_ENCODING = "utf8"


class HomePageView(LoginRequiredMixin, TemplateView):

    template_name = "personal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = list(Account.objects.values(
            'id', 'username', 'email', 'last_login')) * 100
        categories = {
            "Catégorie 1": {
                "Sous-catégorie 1": {
                    "poppers": "#",
                    "tripe à la mode de caen": {
                        "triptease 1": "#",
                        "yeah": "#"
                    }
                },
                "Sous-catégorie 2": "#"},
            "Catégorie 2": "#"
        }
        context['sidebar_menu'] = {"Catégories": categories}

        return context


class ContactView(LoginRequiredMixin, TemplateView):

    template_name = "personal/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_text'] = "Bonjour;Je suis Sébastien votre assistant.;Si vous recherchez un contact je peux vous tâter.;Sinon nique ta mère;"
        return context




@login_required(login_url="login")
def generate_pdf_view(request):
    context = {}
    return generate_pdf(
        "personal/pdf_template.html",
        context,
        f"file_name.pdf",
        download=False,
    )


@login_required(login_url="login")
def download_data_view(request):
    df = pd.DataFrame()
    df.loc["row", "col"] = "Exemple"
    excel_file = BytesIO()
    xlwriter = pd.ExcelWriter(excel_file, engine="xlsxwriter")
    df.to_excel(xlwriter, "sheetname", encoding=EXCEL_ENCODING)
    xlwriter.save()
    xlwriter.close()
    excel_file.seek(0)
    response = HttpResponse(
        excel_file.read(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment; filename=" + EXCEL_FILENAME
    return response
