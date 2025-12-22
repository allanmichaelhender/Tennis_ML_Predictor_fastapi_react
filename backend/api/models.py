from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Predictions(models.Model):
    player1_id=models.BigIntegerField()
    player2_id=models.BigIntegerField()
    match_date = models.DateField(default=datetime.date(2025, 1, 1))
    player1WinOddsLogistic=models.DecimalField(max_digits=20, decimal_places=2, default=0)
    player2WinOddsLogistic=models.DecimalField(max_digits=20, decimal_places=2, default=0)
    player1WinOddsRForest=models.DecimalField(max_digits=20, decimal_places=2, default=0)
    player2WinOddsRForest=models.DecimalField(max_digits=20, decimal_places=2, default=0)
    player1WinOddsDTree=models.DecimalField(max_digits=20, decimal_places=2, default=0)
    player2WinOddsDTree=models.DecimalField(max_digits=20, decimal_places=2, default=0)
    submission_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class Players(models.Model):
    player_id = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name