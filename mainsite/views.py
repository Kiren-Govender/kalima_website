from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "mainsite/index.html")

def about(request):
    return render(request, "mainsite/pages/aboutus.html")

def services(request):
    return render(request, "mainsite/pages/services.html")

def contact(request):
    return render(request, "mainsite/pages/services.html")

def greet(request, name):
    return HttpResponse(f"Hello {name}")