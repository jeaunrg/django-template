from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Account
import copy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


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
def generate_pdf_view(request, slug, download="False"):
    patient = get_object_or_404(Patient, slug=slug)
    SERVER_URL = request.build_absolute_uri("/")
    context = {}
    context["SERVER_URL"] = SERVER_URL
    context["patient"] = patient
    return generate_pdf(
        "personal/pdf_template.html",
        context,
        f"patient_{patient.incl_num}.pdf",
        download == "True",
    )


@login_required(login_url="login")
def download_data_view(request, filter, query):
    kwargs = {}
    if filter == "is_author":
        kwargs["author"] = request.user
    incl_nums = [patient.incl_num for patient in get_patients_queryset(query, **kwargs)]
    queryset = Patient.objects.filter(incl_num__in=incl_nums)
    query = str(queryset.query)
    df = pd.read_sql_query(query, connection)
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
