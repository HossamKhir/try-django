# from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect

# from .forms import RawProductForm
from .forms import ProductForm
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


def render_initial_data(request):
    initial_data = {
        "title": "Awesome",
    }
    # obj = Product.objects.get(id=1)
    form = ProductForm(
        request.POST or None,
        initial=initial_data,
        # instance=obj, # to be able to change a given object
    )
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        "form": form,
    }
    return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    print(request.method)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj,
    }
    return render(request, "products/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()  # list of objects
    context = {
        "object_list": queryset,
    }
    return render(request, "products/product_list.html", context)
