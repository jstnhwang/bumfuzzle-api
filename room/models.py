from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField("Name", max_length=1000)
    is_public = models.BooleanField("Is public")
    password = models.CharField("Password", max_length=50, blank=True, null=True)
    capacity = models.IntegerField("Capacity")

    def __str__(self):
        return self.name