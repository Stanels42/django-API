# from django.views.generic import
from rest_framework import generics
from .models import Album
from .serializers import AlbumSerializers

class AlbumList(generics.ListCreateAPIView):
  queryset = Album.objects.all()
  serializer_class = AlbumSerializers

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Album.objects.all()
  serializer_class = AlbumSerializers
