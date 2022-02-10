from datetime import datetime

from account.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from editable.data import TRAIT_CHOICES
from editable.settings import N_PATIENTS_PER_PAGE

from .forms import (
    PostopPatientFileForm,
    PreopPatientFileForm,
    TraitementFileForm,
    UpdatePatientFileForm,
)
from .models import Patient
from .utils import get_patients_page


class PreopPatientView(LoginRequiredMixin, CreateView):
    form_class = PreopPatientFileForm
    template_name = "patient/preop_patient.html"

    def form_valid(self, form):
        patient = form.save(commit=False)
        patient.author = Account.objects.filter(
            username=self.request.user.username
        ).first()
        patient.save()
        return super(PreopPatientView, self).form_valid(form)

    def get_success_url(self):
        return reverse("patient:detail", kwargs={"slug": self.object.slug})


class PostopPatientView(LoginRequiredMixin, CreateView):
    form_class = PostopPatientFileForm
    template_name = "patient/postop_patient.html"

    def form_valid(self, form):
        patient = form.save(commit=False)
        author = Account.objects.filter(username=self.request.user.username).first()
        patient.author = author
        for k, v in self.request.POST.items():
            for label in ["ddprise_pr", "inobservance"]:
                if k.startswith(label):
                    idtrt = k.split("__")[-1]
                    patient.traitements[idtrt][label] = v
        patient.save()
        return super(PostopPatientView, self).form_valid(form)

    def get_success_url(self):
        return reverse("patient:detail", kwargs={"slug": self.object.slug})


class EditPatientView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = UpdatePatientFileForm
    template_name = "patient/edit_patient.html"

    def get_success_url(self):
        return reverse("patient:detail", kwargs={"slug": self.object.slug})


class DetailPatientView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "patient/detail_patient.html"


class PatientsView(LoginRequiredMixin, TemplateView):
    template_name = "patient/patients.html"

    def get_context_data(self, filter):
        context = {}
        query, patients = get_patients_page(self.request, N_PATIENTS_PER_PAGE, filter)
        context["patients"] = patients
        context["n_patients"] = len(patients)
        context["filter"] = filter
        context["query"] = query
        return context


class AddTraitementView(LoginRequiredMixin, FormView):
    form_class = TraitementFileForm
    template_name = "patient/add_traitement.html"

    def form_valid(self, form):
        patient = get_object_or_404(Patient, slug=self.kwargs["slug"])
        idtrt = 0
        while str(idtrt) in patient.traitements:
            idtrt += 1
        values = {k: v for k, v in self.request.POST.items() if k in form.fields}
        if values["traitement"] in TRAIT_CHOICES:
            values["flags"] = TRAIT_CHOICES[values["traitement"]]
            values["categorie"] = TRAIT_CHOICES[values["traitement"]].split("-")[0]
        patient.traitements[idtrt] = values
        patient.save()
        return super(AddTraitementView, self).form_valid(form)

    def get_success_url(self):
        return reverse("patient:detail", kwargs={"slug": self.kwargs["slug"]})


class EditTraitementView(LoginRequiredMixin, FormView):
    form_class = TraitementFileForm
    template_name = "patient/edit_traitement.html"

    def get_initial(self):
        patient = get_object_or_404(Patient, slug=self.kwargs["slug"])
        return patient.traitements[self.kwargs["idtrt"]]

    def form_valid(self, form):
        idtrt = self.kwargs["idtrt"]
        patient = get_object_or_404(Patient, slug=self.kwargs["slug"])
        if (
            self.request.POST.get("submitType") == "reset"
            and "conclusion" in patient.traitements[idtrt]
        ):
            del patient.traitements[idtrt]["conclusion"]
            patient.save()
        else:
            if self.request.POST.get("submitType") == "delete":
                del patient.traitements[idtrt]
            else:
                values = {
                    k: v for k, v in self.request.POST.items() if k in form.fields
                }
                if values["traitement"] in TRAIT_CHOICES:
                    values["flags"] = TRAIT_CHOICES[values["traitement"]]
                    values["categorie"] = TRAIT_CHOICES[values["traitement"]].split(
                        "-"
                    )[0]
                patient.traitements[idtrt].update(values)
            patient.save()
        return super(EditTraitementView, self).form_valid(form)

    def get_success_url(self):
        return reverse("patient:detail", kwargs={"slug": self.kwargs["slug"]})
