from rest_framework import serializers
from .models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('name','locale','street','legal_entity','website','inn','latitude','longitude')