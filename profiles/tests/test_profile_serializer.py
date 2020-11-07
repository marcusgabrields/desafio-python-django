from django.test import TestCase

from users.models import User

from ..models import Phone, Profile
from ..serializers import ProfileSerializer


class ProfileSerializerTest(TestCase):
    def setUp(self):
        self.profile_data = {
            "first_name": "first",
            "last_name": "last",
            "email": "email@email.com",
            "password": "12345",
            "phones": [
                {"number": 988887888, "area_code": 81, "country_code": "+55"}
            ],
        }

    def test_can_save_a_profile_with_user(self):
        serializer = ProfileSerializer(data=self.profile_data)
        self.assertTrue(serializer.is_valid())

        serializer.save()
        self.assertTrue(Profile.objects.exists())
        self.assertTrue(User.objects.exists())

    def test_can_save_a_profile_with_phones(self):
        serializer = ProfileSerializer(data=self.profile_data)
        self.assertTrue(serializer.is_valid())

        serializer.save()
        self.assertTrue(Phone.objects.exists())
    
    def test_repited_email(self):
        serializer_1 = ProfileSerializer(data=self.profile_data)
        self.assertTrue(serializer_1.is_valid())
        serializer_1.save()

        serializer_2 = ProfileSerializer(data=self.profile_data)
        self.assertFalse(serializer_2.is_valid())
