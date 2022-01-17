from django import forms
from django.contrib.auth import authenticate
from .models import Account
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from mysite.widgets import MyCroppieField


IMG_OPTIONS = {
    'viewport': {
        'width': 180,
        'height': 180,
        'shape': 'circle'
        },
    }

class SignupForm(UserCreationForm):
    profile_picture = MyCroppieField(label="Photo de profil", options=IMG_OPTIONS, required=False)

    class Meta:
        model = Account
        fields = ('profile_picture', 'username', 'email')


class AccountUpdateForm(UserChangeForm):
    profile_picture = MyCroppieField(label="Photo de profil", options=IMG_OPTIONS, required=False)

    class Meta:
        model = Account
        fields = ('profile_picture', 'username', 'email')
