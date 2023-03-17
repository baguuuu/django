from rest_framework import serializers
from restapi.models import Configuration, Usrs, Grp

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'

class UsrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usrs
        fields = '__all__'

class GrpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grp
        fields = '__all__'
