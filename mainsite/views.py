from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "mainsite/index.html")

def test(request):
    return HttpResponse("Hello Test")

def greet(request, name):
    return HttpResponse(f"Hello {name}")