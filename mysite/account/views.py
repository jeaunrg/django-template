from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import AccountUpdateForm, SignupForm
from .models import Account


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AccountUpdateForm
    template_name = "account/update.html"
    success_url = "/account/update"

    def get_object(self, queryset=None):
        return self.request.user


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = "/"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "account/signup.html"
    success_url = "/"


class SigninView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)
