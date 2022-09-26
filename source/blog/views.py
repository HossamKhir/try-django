from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ArticleModelForm

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


class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # NOTE: by default, on success the app redirects to the url of the newly
    #   created instance, hence the get_absolute_url method should be
    #   implemented on the model
    # NOTE: to override that either set success_url or implement get_success_url
    # success_url = "/"

    def form_valid(self, form):
        # print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self) -> str:
    #     return "/"


class ArticleUpdateView(UpdateView):
    template_name = "articles/article_create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Article, id=_id)


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"
    # queryset = Article.objects.all()

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Article, id=_id)

    def get_success_url(self) -> str:
        return reverse("blog:article-list")
