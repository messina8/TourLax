from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Tournament(models.Model):

    class TournamentType(models.TextChoices):
        LEAGUE = 'LE', _('League')
        DIRECT_ELIMINATION = 'DE', _('Direct Elimination')

    name = models.CharField(max_length=80)
    players = models.IntegerField()
    creator = models.ManyToOneRel(User, on_delete=models.CASCADE, field_name="owner", to=User.username)
    organizer = models.CharField(max_length=70)
    admins = models.ManyToManyRel(User, to=User.username)
    voters = models.ManyToManyRel(User, to=User.username)
    type = models.CharField(max_length=2, choices=TournamentType.choices)


class Player(models.Model):
    name = models.CharField(max_length=70)


class Match(models.Model):
    tournament = models.ManyToOneRel(Tournament, on_delete=models.CASCADE, field_name='tournament', to=Tournament.name)
    score = models.JSONField()
    players = models.ManyToManyRel(Player, to=Player.name)

