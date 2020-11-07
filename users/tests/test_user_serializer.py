from django.test import TestCase

from ..models import User
from ..serializers import UserSerializer


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {"email": "email@email.com", "password": "12345"}

    def test_can_save_a_user(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())

        serializer.save()
        self.assertTrue(User.objects.exists())

    def test_encripty_password_when_save(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())

        user = serializer.save()
        self.assertFalse(user.password == self.user_data.get("password"))
