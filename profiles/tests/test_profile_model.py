from django.db.utils import IntegrityError
from django.test import TestCase
from model_bakery import baker

from ..models import Profile


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = baker.make("users.User")

    def test_can_create_a_profile(self):
        Profile.objects.create(
            user=self.user, first_name="Fristname", last_name="Lastname"
        )
        self.assertTrue(Profile.objects.exists())

    def test_can_create_a_profile_with_same_user(self):
        Profile.objects.create(
            user=self.user, first_name="Fristname", last_name="Lastname"
        )
        self.assertTrue(Profile.objects.exists())

        with self.assertRaises(IntegrityError):
            Profile.objects.create(
                user=self.user, first_name="Fristname", last_name="Lastname"
            )
