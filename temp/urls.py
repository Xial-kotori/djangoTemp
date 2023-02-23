from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add-person', views.add_person)
]
