from django.db.utils import IntegrityError
from django.test import TestCase

from ..models import User


class UserModelTest(TestCase):
    def test_can_create_a_user(self):
        User.objects.create(email='email@email.com')
        self.assertTrue(User.objects.exists())
    
    def test_can_create_duplicated_user_email(self):
        User.objects.create(email='email@email.com')
        self.assertTrue(User.objects.exists())

        with self.assertRaises(IntegrityError):
            User.objects.create(email='email@email.com')
