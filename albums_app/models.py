from django.db import models
from musicians_app.models import Musician
# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=20)
    singer = models.OneToOneField(Musician, on_delete=models.CASCADE, default =None)
    release_date = models.DateField()
    def __str__(self):
        return f'{self.album_name}'