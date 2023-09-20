from django.db import models

class Cinema(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    locale = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name