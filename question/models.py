from django.db import models
from room.models import Room

class Question(models.Model):
    description = models.CharField("Description", max_length=1000)
    answer = models.CharField("Answer", max_length=500)
    category = models.CharField("Category", max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
