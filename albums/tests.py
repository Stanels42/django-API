from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Album

class AlbumTest(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(
      username='testuser',
      email='test@email.com',
      password='secret'
    )
    self.data = Album.objects.create(
      title='title',
      artist='name',
      tracks=10,
    )

  def test_list_page(self):
    responce = self.client.get(reverse('api_list'))
    self.assertContains(responce, 'name')

  def test_detail_page(self):
    failed_responce = self.client.get('/albums/100000')
    self.assertEqual(failed_responce.status_code, 404)

  def test_why_does_this_fail(self):
    responce = self.client.get('albums/1/')
    self.assertEqual(responce.status_code, 200)

