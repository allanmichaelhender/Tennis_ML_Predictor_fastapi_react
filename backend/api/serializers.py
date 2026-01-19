from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Predictions, Players
import datetime

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
        }

class PredictionsGuestSerializer(serializers.Serializer):
    player1_id = serializers.IntegerField()
    player2_id = serializers.IntegerField()
    match_date = serializers.DateField(default=datetime.date(2025, 1, 1))
    player1WinOddsLogistic = serializers.DecimalField(
        max_digits=20, decimal_places=3, default=0
    )
    player2WinOddsLogistic = serializers.DecimalField(
        max_digits=20, decimal_places=3, default=0
    )
    player1WinOddsRForest = serializers.DecimalField(
        max_digits=20, decimal_places=3, default=0
    )
    player2WinOddsRForest = serializers.DecimalField(
        max_digits=20, decimal_places=3, default=0
    )
    player1WinOddsDTree = serializers.DecimalField(
        max_digits=20, decimal_places=3, default=0
    )
    player2WinOddsDTree = serializers.DecimalField(
        max_digits=20, decimal_places=3, default=0
    )

class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'

    extra_kwargs = {
        "player_id": { "read_only": True },
        "full_name": { "read_only": True },
    }
