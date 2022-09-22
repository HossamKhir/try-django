from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(req, *args, **kwargs):
    print(req.user)
    # return HttpResponse("<h1>Hello, World!</h1>")
    return render(req, "home.html", {})


def contact_view(req, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(req, "contact.html", {})



def about_view(req, *args, **kwargs):
    # return HttpResponse("<h1>About Page</h1>")
    return render(req, "about.html", {})

