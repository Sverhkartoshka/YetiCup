from django.contrib import admin

from .models import User, Championship, Team, Participant, Score

admin.site.register(User)
admin.site.register(Championship)
admin.site.register(Team)
admin.site.register(Participant)
admin.site.register(Score)

