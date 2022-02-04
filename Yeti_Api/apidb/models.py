from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    School = models.CharField(max_length=250)

class Championship(models.Model):
    championship_id = models.IntegerField(primary_key=True)
    championship_name = models.CharField(max_length=100)
    championship_picture = models.ImageField(null=True, blank=True, editable=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    date_id = models.DateField()
    location = models.CharField(max_length=250)

class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=30)

class Participant(models.Model):
    participant_id = models.IntegerField(primary_key=True)
    championship_id = models.ForeignKey(Championship, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=15)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Score(models.Model):
    event_id = models.IntegerField(primary_key=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    championship_id = models.ForeignKey(Championship, on_delete=models.CASCADE)
    score = models.IntegerField()