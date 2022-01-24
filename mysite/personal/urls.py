from django.urls import path
from .views import ContactView, ArtistView, AssociationView


app_name = 'personal'

urlpatterns = [
    path('contact/', ContactView.as_view(), name="contact"),
    path('artist/', ArtistView.as_view(), name="artist"),
    path('association/', AssociationView.as_view(), name="association"),

]
