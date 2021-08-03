from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def new_register(request):
    return render(request, 'myApp/new_register.html', {})

