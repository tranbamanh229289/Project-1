from django.db import models

# Create your models here.
class Article(models.Model):
    id_article = models.CharField(max_length=10)
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=32765)