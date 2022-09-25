from django.urls import reverse
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"id": self.id})
