from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


class SignupViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("signup")

    def test_get_status_code_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code
        )

    def test_put_status_code_not_allowed(self):
        response = self.client.put(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code
        )

    def test_patch_status_code_not_allowed(self):
        response = self.client.patch(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code
        )

    def test_delete_status_code_not_allowed(self):
        response = self.client.delete(self.url)
        self.assertEqual(
            status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code
        )

    def test_post_status_code_without_payload(self):
        response = self.client.post(self.url)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_post_status_code_with_invalid_payload(self):
        payload = {"first_name": "first", "password": "12345"}
        response = self.client.post(self.url, payload)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_post_status_code_with_valid_payload(self):
        payload = {
            "first_name": "first",
            "last_name": "last",
            "email": "email@email.com",
            "password": "12345",
            "phones": [
                {"number": 988887888, "area_code": 81, "country_code": "+55"}
            ],
        }
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
