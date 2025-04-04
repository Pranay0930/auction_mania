from django.test import TestCase
#from django.contrib.auth.models import UserManager
from django.urls import reverse
from auction_app.models import UserModel

class LoginTestCase(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.email = "testemail@gmail.com"
        self.user = UserModel.objects.create_user(username=self.username,email=self.email, password=self.password)

    def test_login_successful(self):
        response = self.client.post(reverse('login_page'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('user_auctions_list'))
