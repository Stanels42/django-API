from rest_framework import serializers
from .models import Album

class AlbumSerializers(serializers.ModelSerializer):
  class Meta:
    model = Album
    fields = [
      'id',
      'title',
      'artist',
      'tracks',
      'user',
      ]
