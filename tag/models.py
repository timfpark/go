from django.db import models

class TagEntry(models.Model):
    tag = models.CharField(max_length=256)
    url = models.CharField(max_length=2048)
