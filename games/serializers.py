from rest_framework import serializers
from games.models import Game

class GameSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only = True)
    