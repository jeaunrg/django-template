from django import forms
from patient.models import Patient


class PatientAlgoForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "algo_conclusions",
            "algo_complete_results",
        ]
