from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(req, *args, **kwargs):
    print(req.user)
    return HttpResponse("<h1>Hello, World!</h1>")


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")


def about_view(*args, **kwargs):
    return HttpResponse("<h1>About Page</h1>")
