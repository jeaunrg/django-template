from django import forms
from editable.data import *

from .models import Patient, to_choice


class CustomModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_input_types()

    def init_input_types(self):
        for field in self:
            if isinstance(field.field, (forms.fields.DateField)):
                field.input_type = "date"
            else:
                field.input_type = field.field.widget.input_type


class TraitementFileForm(forms.Form):
    pathologie = forms.ChoiceField(
        label="Pathologie justifiant le traitement",
        choices=to_choice(PATH_CHOICES, False),
    )
    traitement = forms.ChoiceField(
        label="Traitement", choices=to_choice(TRAIT_CHOICES, False)
    )
    ddprise_th = forms.DateField(
        label="Date de dernière prise théorique", required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_input_types()

    def init_input_types(self):
        for field in self:
            if isinstance(field.field, (forms.fields.DateField)):
                field.input_type = "date"
            else:
                field.input_type = field.field.widget.input_type


class PreopPatientFileForm(CustomModelForm):
    class Meta:
        model = Patient
        fields = [
            "firstname",
            "lastname",
            "height",
            "weight",
            "ddn",
            "chirurgie",
            "ddi",
            "intervention",
            "chirurgien",
            "bleeding_risk",
        ]


class PostopPatientFileForm(CustomModelForm):
    class Meta:
        model = Patient
        fields = [
            "schema_therap",
            "aptt",
            "pt",
            "inr",
            "hemoglobine",
            "plaquette",
            "dfg",
            "vol_sang",
            "coag",
        ]

    def save(self, commit=True):
        patient = self.instance

        if commit:
            patient.save()
        return patient

    def get_inobservance_choices(self):
        return [
            "Pas d'inobservance",
            "Oubli",
            "Incompréhension",
            "Contre-ordre médical",
        ]


class UpdatePatientFileForm(CustomModelForm):
    class Meta:
        model = Patient
        fields = [
            "firstname",
            "lastname",
            "height",
            "weight",
            "ddn",
            "ddi",
            "intervention",
            "chirurgien",
            "chirurgie",
            "bleeding_risk",
            "schema_therap",
            "aptt",
            "pt",
            "inr",
            "hemoglobine",
            "plaquette",
            "dfg",
            "vol_sang",
            "coag",
        ]

    def save(self, commit=True):
        patient = self.instance

        if commit:
            patient.save()
        return patient
