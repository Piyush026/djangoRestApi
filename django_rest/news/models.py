from django.db import models


# Create your models here.

class News(models.Model):
    category = models.CharField(max_length=100)
    heading = models.CharField(max_length=300, unique=True)
    news = models.CharField(max_length=1500,)
    published_by = models.CharField(max_length=100)
    file = models.FileField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
