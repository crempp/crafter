from crafter.models import (
    Player,
    Game,
)

from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


# Serializers define the API representation.
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = (
            'url',
            'name',
            'uuid'
        )


class GameSerializer(serializers.HyperlinkedModelSerializer):
    version = serializers.RelatedField(many=False)

    map_url = serializers.CharField(source='map_url', read_only=True)
    player_status = serializers.CharField(source='player_status', read_only=True)
    server_status = serializers.CharField(source='server_status', read_only=True)
    player_count_string = serializers.CharField(source='player_count_string', read_only=True)
    online_player_list = serializers.CharField(source='online_player_list', read_only=True)

    class Meta:
        model = Game
        fields = (
            'url',
            'name',
            'description',
            'version',
            'online',
            'online_players',

            'map_url',
            'player_status',
            'server_status',
            'player_count_string',
            'online_player_list',
        )


# ViewSets define the view behavior.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action()
    def start(self, request, pk=None):
        print("Starting")
        return Response([])

    @action()
    def stop(self, request, pk=None):
        print("Stopping")
        return Response([])

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'player', PlayerViewSet)
router.register(r'game', GameViewSet)