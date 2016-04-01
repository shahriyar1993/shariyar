from PremierLeagueAPI.models import AllClubs, AllManager, AllPlayers, AllStadium, AllTrophies
from rest_framework import serializers

class ClubsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllClubs
        fields = ('id', 'name')

class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllManager
        fields = ('id', 'name','nationality')

class PlayersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllPlayers
        fields = ('id', 'name','nationality')

class StadiumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllStadium
        fields = ('id', 'capacity', 'location')

class TrophiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllTrophies
        fields = ('id', 'name', 'notrophies')
