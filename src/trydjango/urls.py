"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from pages.views import about_view, contact_view, home_view

# from products.views import (
#     product_detail_view,
#     product_create_view,
#     render_initial_data,
#     dynamic_lookup_view,
#     product_delete_view,
#     product_list_view,
#     product_update_view,
# )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("contact/", contact_view),
    path("about/", about_view),
    # path("product/", product_detail_view),
    # path("create/", product_create_view),
    # path("create/", render_initial_data),
    # path("product/<int:id>/", dynamic_lookup_view, name="product-detail"),
    # path("product/<int:id>/delete/", product_delete_view, name="product-delete"),
    # path("products/", product_list_view),
    # path("product/<int:id>/update", product_update_view, name="product-update"),
    path("products/", include("products.urls")),
    path("blog/", include("blog.urls")),
    path("course/", include("courses.urls")),
]
