from django import forms
from catalogue.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['titre', 'image', 'no_inventaire', 'categorie', 'theme',
                  'technique', 'support', 'region', 'lieu', 'dimensions',
                  'epoque', 'type_collection', 'droits', 'tags', 'description']
