from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("places/<int:id>/", views.location_detail, name="location_detail"),
]
