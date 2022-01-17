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
            'id', 'username', 'email', 'is_admin', 'last_login')) * 100
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
