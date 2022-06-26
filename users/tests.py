from django.test import Client, TestCase
from django.contrib.auth import get_user_model, authenticate, get_user
from django.urls import reverse
from django.utils import timezone

from pprint import pprint

# Create your tests here.
class UserDetailPageTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='username', password='password', birth_date=timezone.now())
        self.user.save()
        

    def test_user_detail_page_status_code(self):
        # client = Client()
        self.client.login(username='username', password='password')
        response = self.client.get(reverse('user_detail', kwargs={'pk':self.user.pk}))
        self.assertEqual(response.status_code, 200)

    def test_user_detail_edit_button(self):
        self.client.login(username='username', password='password')
        response = self.client.get(reverse('user_detail', kwargs={'pk':self.user.pk}))
        self.assertContains(response, f'/users/{self.user.pk}/update')
        self.assertContains(response, 'Редактировать')
        
