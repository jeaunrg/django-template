from django import forms
from django.contrib.auth import authenticate
from .models import Account
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from mysite.widgets import MyCroppieField


class SignupForm(UserCreationForm):
    profile_picture = MyCroppieField(label="Photo de profil", required=False)

    class Meta:
        model = Account
        fields = ('profile_picture', 'username', 'email')


class AccountUpdateForm(UserChangeForm):
    profile_picture = MyCroppieField(label="Photo de profil", required=False)

    class Meta:
        model = Account
        fields = ('profile_picture', 'username', 'email')
