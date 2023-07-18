from django.contrib.auth import get_user_model
from match_users.models import Matches
from rest_framework import serializers

User = get_user_model()


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'sex', 'photo')


class MatchesSerializer(serializers.ModelSerializer):
    like = serializers.BooleanField()

    class Meta:
        model = Matches
        fields = ('like',)
