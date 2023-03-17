from django.shortcuts import render
from rest_framework import viewsets

from restapi.models import Configuration, Usrs, Grp
from restapi.serializer import ConfigurationSerializer, UsrsSerializer, GrpSerializer
# Create your views here.

class ConfigurationViewSet(viewsets.ModelViewSet):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer

class UsrsViewSet(viewsets.ModelViewSet):
    queryset = Usrs.objects.all()
    serializer_class = UsrsSerializer

class GrpViewSet(viewsets.ModelViewSet):
    queryset = Grp.objects.all()
    serializer_class = GrpSerializer

