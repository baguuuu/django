from django.shortcuts import render
from rest_framework import viewsets

from models import Configuration, Usrs, Grp
from serializer import ConfigurationSerializer, UsrsSerializer, GrpSerializer
# Create your views here.

class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer

class UsrsViewSet(viewsets.ModelViewSet):
    queryset = UsrsSerializer.objects.all()
    serializer_class = UsrsSerializer

class GrpViewSet(viewsets.ModelViewSet):
    queryset = GrpSerializer.objects.all()
    serializer_class = GrpSerializer

