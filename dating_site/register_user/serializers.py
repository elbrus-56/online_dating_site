from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    photo = serializers.ImageField(default="images/default.png")

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  'sex',
                  'password',
                  'photo')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(CreateUserSerializer, self).create(validated_data)


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',
                  'password')
