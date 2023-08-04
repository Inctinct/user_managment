from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user.models import RegisteredUser


class RegistrationSerializer(ModelSerializer):
    """
    Serializer for user registration. It defines the necessary fields
    and provides a method to create a new registered user.
    """

    password = serializers.CharField(max_length=100, min_length=8, write_only=True)

    class Meta:
        model = RegisteredUser
        fields = ["email", "password", "phone", "first_name", "second_name"]

    def create(self, validated_data):
        """
        Creates a new user instance using the validated data.

        :param validated_data: The validated data for the user
        :return: A user object
        """
        return RegisteredUser.objects.create_user(**validated_data)


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = ["email", "phone", "first_name", "second_name"]
