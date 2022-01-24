from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Account
import copy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):

    template_name = "personal/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = list(Account.objects.values(
            'id', 'username', 'email', 'is_admin', 'last_login')) * 100
        return context


class ContactView(TemplateView):

    template_name = "personal/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_text'] = "Bonjour;Je suis Sébastien votre assistant.;Si vous recherchez un contact je peux vous tâter.;Sinon nique ta mère;"
        return context


class ArtistView(TemplateView):
    template_name = "personal/artist.html"


class AssociationView(TemplateView):
    template_name = "personal/association.html"
