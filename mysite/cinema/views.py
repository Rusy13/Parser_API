from django.shortcuts import render
from rest_framework import generics
from .models import Cinema
from .serializers import CinemaSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class CinemaApiV(generics.ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['id', 'name', 'locale', 'website', 'email',]