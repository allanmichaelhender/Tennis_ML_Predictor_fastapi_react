from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Predictions, Players

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user
    

class PredictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predictions
        fields = '__all__'

    extra_kwargs = {
        "author": { "read_only": True },
        "submission_date": { "read_only": True },
        "Player1WinOdds": { "read_only": True },
        "Player2WinOdds": { "read_only": True },
    }

class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'

    extra_kwargs = {
        "PlayerID": { "read_only": True },
        "full_name": { "read_only": True },
    }
