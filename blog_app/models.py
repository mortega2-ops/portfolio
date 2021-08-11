from django.db import models
from markdownx.models import MarkdownxField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = MarkdownxField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
