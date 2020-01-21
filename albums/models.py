from django.db import models

class Album(models.Model):
  title = models.CharField(max_length=128)
  artist = models.CharField(max_length=128)
  tracks = models.IntegerField()

  def __str__(self):
    return self.title
