from django.urls import path

from .views import AlgoView, algo_view

app_name = "algorithm"

urlpatterns = [
    path("<slug>/<mode>/algo/", AlgoView.as_view(), name="algo"),
]
