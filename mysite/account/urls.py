from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, PasswordChangeView
from .views import (
    SigninView,
    SignupView,
    AccountUpdateView,
    AccountDeleteView,
    )


app_name = 'account'

urlpatterns = [
    path('login/', SigninView.as_view(template_name='account/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('update/', AccountUpdateView.as_view(), name="update"),
    path('<pk>/delete/', AccountDeleteView.as_view(), name="delete"),
    path('password/', PasswordChangeView.as_view(template_name='account/change_password.html'), name="password"),
]
