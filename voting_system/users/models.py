from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class VotingUser(models.Model):
    name = models.CharField(max_length=8)
    qr_code = models.CharField(max_length=32)
    vote_first_king = models.PositiveIntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(1)])
    vote_first_queen = models.PositiveIntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(1)])
    vote_king = models.PositiveIntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(1)])
    vote_queen = models.PositiveIntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(1)])
    

    def __str__(self):
        return self.name