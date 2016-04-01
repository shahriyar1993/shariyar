from PremierLeagueAPI.models import AllClubs, AllManager, AllPlayers, AllStadium, AllTrophies
from rest_framework import viewsets
from PremierLeagueAPI.serializers import ClubsSerializer, ManagerSerializer, PlayersSerializer, StadiumSerializer, TrophiesSerializer

# Create your views here.

class AllClubsSet(viewsets.ModelViewSet):

    queryset = AllClubs.objects.all()
    serializer_class = ClubsSerializer

class AllManagerSet(viewsets.ModelViewSet):

    queryset = AllManager.objects.all()
    serializer_class = ManagerSerializer

class AllPlayersSet(viewsets.ModelViewSet):

    queryset = AllPlayers.objects.all()
    serializer_class = PlayersSerializer

class AllStadiumSet(viewsets.ModelViewSet):

    queryset = AllStadium.objects.all()
    serializer_class = StadiumSerializer

class AllTrophiesSet(viewsets.ModelViewSet):

    queryset = AllTrophies.objects.all()
    serializer_class = TrophiesSerializer