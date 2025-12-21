from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Predictions(models.Model):
    player1ID=models.BigIntegerField()
    player2ID=models.BigIntegerField()
    match_date = models.DateField(default=datetime.date(2025, 1, 1))
    player1WinOdds=models.DecimalField(max_digits=20, decimal_places=2)
    player2WinOdds=models.DecimalField(max_digits=20, decimal_places=2)
    submission_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class Players(models.Model):
    playerID = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name