from django.contrib import admin

import tournaments.models

# Register your models here.

admin.site.register(tournaments.models.Tournament)
admin.site.register(tournaments.models.Player)
admin.site.register(tournaments.models.Match)
