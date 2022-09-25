from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
)

app_name = "blog"

urlpatterns = [
    path("", ArticleListView.as_view(), name="article-list"),
    # path("<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("create/", ArticleCreateView.as_view(), name="article-create"),
    path("<int:id>/", ArticleDetailView.as_view(), name="article-detail"),
    path("<int:id>/update", ArticleUpdateView.as_view(), name="article-update"),
]
