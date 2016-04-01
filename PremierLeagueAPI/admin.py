from django.contrib import admin
from PremierLeagueAPI.models import AllClubs, AllManager, AllPlayers, AllStadium, AllTrophies

# Register your models here.

class ClubsAd(admin.ModelAdmin):

    list_display = ['id','name']

class ManagerAd(admin.ModelAdmin):

    list_display = ['id','name','nationality']


class PlayersAd(admin.ModelAdmin):

    list_display = ['id','name','nationality']

class StadiumAd(admin.ModelAdmin):

    list_display = ['id', 'capacity', 'location']
    
class TrophiesAd(admin.ModelAdmin):

    list_display = ['id', 'name', 'notrophies']


admin.site.register(AllClubs, ClubsAd)
admin.site.register(AllManager, ManagerAd)
admin.site.register(AllPlayers, PlayersAd)
admin.site.register(AllStadium, StadiumAd)
admin.site.register(AllTrophies, TrophiesAd)
