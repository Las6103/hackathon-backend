from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=1200)
    issued = models.CharField(max_length=1200)

    def __str__(self):
        return self.title
