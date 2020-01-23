from django.urls import path, include
from .views import AlbumList, AlbumDetail

urlpatterns = [
  path('albums/', AlbumList.as_view(),name='api_list'),
  path('albums/<int:pk>/', AlbumDetail.as_view(),name='detail'),
]
