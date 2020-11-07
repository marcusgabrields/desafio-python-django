from django.db.utils import IntegrityError
from rest_framework import serializers

from users.models import User

from .models import Phone, Profile


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = [
            "profile",
            "number",
            "area_code",
            "country_code",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    phones = serializers.ListField(write_only=True)

    class Meta:
        model = Profile
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "phones",
        ]

    def create(self, validated_data):
        phones_data = validated_data.pop("phones")
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        user = User(email=email)
        user.set_password(password)
        user.save()

        profile = Profile.objects.create(user=user, **validated_data)
        for phone in phones_data:
            Phone.objects.create(profile=profile, **phone)

        return profile

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("E-mail already exists")

        return email
