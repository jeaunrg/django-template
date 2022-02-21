from django import forms
from editable.data import *

from .models import Patient, to_choice


class CustomForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_input_types()

    def init_input_types(self):
        for field in self:
            if isinstance(field.field, (forms.fields.DateField)):
                field.input_type = "date"
            else:
                field.input_type = field.field.widget.input_type


class PreopPatientFileForm(CustomForm, forms.ModelForm):
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


class PostopPatientFileForm(CustomForm, forms.ModelForm):
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

    def get_inobservance_choices(self):
        return [
            "Pas d'inobservance",
            "Oubli",
            "Incompréhension",
            "Contre-ordre médical",
        ]


class UpdatePatientFileForm(CustomForm, forms.ModelForm):
    class Meta:
        model = Patient
        fields = PreopPatientFileForm.Meta.fields + PostopPatientFileForm.Meta.fields


class TraitementFileForm(CustomForm):
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
