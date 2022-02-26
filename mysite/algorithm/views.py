import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import UpdateView
from editable.algorithm import ALGO
from editable.data import REFS
from editable.default import get_default_results
from editable.questions import QUESTIONS
from patient.models import Patient

from .forms import PatientAlgoForm
from .models import Algorithm
from .utils import get_algo
from django.urls import reverse


def get_algo(name="Default"):
    algo = Algorithm.objects.filter(name=name).first()
    if algo is None:
        algo = Algorithm(name=name)
        algo.save()
    return algo

class AlgoView(LoginRequiredMixin, UpdateView):
    template_name = "algorithm/algo_manager.html"
    form_class = PatientAlgoForm
    model = Patient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        algo = get_algo()
        context.update(algo.build())
        return context

    def get_success_url(self):
        return reverse("patient:detail", kwargs={"slug": self.object.slug})



@login_required(login_url="login")
def algo_view(request, slug, mode):
    context = {}
    patient = get_object_or_404(Patient, slug=slug)
    context["patient"] = patient

    if request.POST:
        results = {}
        conclusions = {}
        for k, v in request.POST.items():
            if k.startswith("RESULTS"):
                results[k[8:]] = v
                if k[8:] in patient.__dict__:
                    patient.__dict__[k[8:]] = v
            elif k.startswith("CONCLUSIONS"):
                conclusions[k[12:]] = v
        patient.algo_complete_results = results
        # empty conclusions
        patient.reset_cure_conclusions()
        for k, v in conclusions.items():
            if k in REFS:
                traitement_ids = patient.get_traitement_ids(**REFS[k])
                for i in traitement_ids:
                    patient.traitements[i]["conclusion"].append(v)

        patient.save()
        return redirect("patient:detail", slug)

    default_results = {}
    context["refs"] = REFS
    context["algo"], context["pbar_max"] = get_algo()
    context["questions"] = QUESTIONS
    if mode == "from_scratch":
        context["results"] = {}
    else:
        context["results"] = get_default_results(patient)
    return render(request, "algorithm/algo_manager.html", context)
