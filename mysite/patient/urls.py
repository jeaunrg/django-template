from django.urls import path

from .views import (
    AddTraitementView,
    DetailPatientView,
    EditPatientView,
    EditTraitementView,
    PatientsView,
    PostopPatientView,
    PreopPatientView,
)

app_name = "patient"


urlpatterns = [
    path("preop/", PreopPatientView.as_view(), name="preop"),
    path("patients/<filter>/", PatientsView.as_view(), name="patients"),
    path("postop/<slug>/", PostopPatientView.as_view(), name="postop"),
    path("<slug>/", DetailPatientView.as_view(), name="detail"),
    path("<slug>/edit/", EditPatientView.as_view(), name="edit"),
    path("<slug>/addtrt/", AddTraitementView.as_view(), name="addtrt"),
    path("<slug>/<idtrt>/edittrt/", EditTraitementView.as_view(), name="edittrt"),
]
