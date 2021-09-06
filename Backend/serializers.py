from rest_framework import serializers
from .models import *

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        Model = Service
        field= "__all__"
