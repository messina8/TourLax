from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=50)
    players = models.IntegerField()
    organizer = models.ManyToOneRel(User, on_delete=models.CASCADE, field_name="owner", to=User.username)
    admins = models.ForeignKey(User, default=organizer, on_delete=models.SET_DEFAULT)
    voters = models.ForeignKey(User, to=name, null=True, blank=True, on_delete=models.SET_NULL)

class Match(models.Model):
    tournament = models.ManyToOneRel(Tournament, on_delete=models.CASCADE, field_name='tournament', to=Tournament.name)

