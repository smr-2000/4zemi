from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_register, name='new_register'),
]
