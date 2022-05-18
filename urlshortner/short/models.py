from django.db import models

class Http(models.Model):
    shortened = models.CharField(max_length=250)
    original = models.CharField(max_length=1000)

    def __str__(self):
        return self.shortened
