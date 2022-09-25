from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

# Create your views here.
from .models import Article


class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    # NOTE: queryset here limits the choices for the detail view
    # queryset = Article.objects.all()

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Article, id=_id)
