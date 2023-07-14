from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    photo = serializers.ImageField(default="images/default.png")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'sex', 'password', 'photo')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(CreateUserSerializer, self).create(validated_data)

