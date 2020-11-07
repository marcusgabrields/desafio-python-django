from django.test import TestCase
from model_bakery import baker

from ..models import Phone
from ..serializers import PhoneSerializer


class PhoneSerializerTest(TestCase):
    def setUp(self):
        self.profile = baker.make('profiles.Profile')

    def test_can_create_a_phone(self):
        phone_data = {
            "profile": self.profile.id,
            "number": 988887888,
            "area_code": 81,
            "country_code": "+55",
        }
        serialzier = PhoneSerializer(data=phone_data)

        self.assertTrue(serialzier.is_valid())

        serialzier.save()
        self.assertTrue(Phone.objects.exists())
