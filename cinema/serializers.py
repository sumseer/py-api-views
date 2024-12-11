from rest_framework import serializers

from cinema.models import (
    Movie,
    Actor,
    Genre,
    CinemaHall
)


class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration"]


class ActorSerializer(serializers.Serializer):
    class Meta:
        model = Actor
        fields = ["first_name", "last_name"]


class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        fields = ["name"]


class CinemaHallSerializer(serializers.Serializer):
    class Meta:
        model = CinemaHall
        fields = ["name", "rows", "seats_in_row"]
