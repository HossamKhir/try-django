from django.shortcuts import render

from .forms import ProductForm, RawProductForm
from .models import Product


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    # }
    context = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        # to clear the form
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     if request.method == "POST":
#         new_title = request.POST.get("title")
#         print(new_title)
#         # Product.objects.create(title=new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == "POST":
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         "form": form,
#     }
#     return render(request, "products/product_create.html", context)
