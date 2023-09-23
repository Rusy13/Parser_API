from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=255)
    locale = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    legal_entity = models.CharField(max_length=255)
    website = models.URLField(null=True, blank=True)
    inn = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)

    def __str__(self):
        return self.name