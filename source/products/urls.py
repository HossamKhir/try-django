from django.urls import path
from .views import (
    render_initial_data,
    product_delete_view,
    # product_detail_view,
    product_list_view,
    product_update_view,
    dynamic_lookup_view,
)

app_name = "products"
urlpatterns = [
    # path("", product_detail_view),
    # path("create/", product_create_view),
    path("", product_list_view, name="product-list"),
    path("create/", render_initial_data),
    path("<int:id>/", dynamic_lookup_view, name="product-detail"),
    path("<int:id>/delete/", product_delete_view, name="product-delete"),
    path("<int:id>/update", product_update_view, name="product-update"),
]
