from django.shortcuts import render
from rest_framework import generics
from .models import Cinema
from .serializers import CinemaSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CinemaApiV(generics.ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['name', 'locale', 'street', 'legal_entity', 'website','inn','latitude','longitude']

    @swagger_auto_schema(
    operation_description="Список кинотеатров",
    responses={200: CinemaSerializer(many=True)},
    manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, description="Название кинотеатра", type=openapi.TYPE_STRING),
        openapi.Parameter('locale', openapi.IN_QUERY, description="Локация", type=openapi.TYPE_STRING),
        openapi.Parameter('street', openapi.IN_QUERY, description="Улица", type=openapi.TYPE_STRING),
        openapi.Parameter('legal_entity', openapi.IN_QUERY, description="Юр лицо", type=openapi.TYPE_STRING),
        openapi.Parameter('website', openapi.IN_QUERY, description="Сайт", type=openapi.TYPE_STRING),
        openapi.Parameter('inn', openapi.IN_QUERY, description="ИНН", type=openapi.TYPE_STRING),
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Широта", type=openapi.TYPE_STRING),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Долгота", type=openapi.TYPE_STRING),
        # Добавьте описание для других параметров фильтрации
    ])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)