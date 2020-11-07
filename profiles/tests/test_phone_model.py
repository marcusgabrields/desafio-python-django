from django.db.utils import IntegrityError
from django.test import TestCase
from model_bakery import baker

from ..models import Phone


class PhoneModelTest(TestCase):
    def setUp(self):
        self.profile = baker.make('profiles.Profile')

    def test_can_create_a_phone(self):
        Phone.objects.create(
            profile=self.profile,
            number=999999999,
            area_code=99,
            country_code="+55",
        )
