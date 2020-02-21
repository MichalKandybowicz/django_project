from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>Hello World</h1>")


def contact(request, *args, **kwargs):
    return HttpResponse("<h1>any@any.any</h1>")


def shop(request, *args, **kwargs):
    return HttpResponse("<h1>shop</h1>")

