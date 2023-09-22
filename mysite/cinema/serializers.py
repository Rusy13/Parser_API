from rest_framework import serializers
from .models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ('id','name','locale','website','email')