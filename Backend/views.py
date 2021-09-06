from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import *

# import the serializers 
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



# Create your views here


class ServicesView(APIView):
    def get(self, request):
        services = Service.objects.get(pk=1)
        ser_services = ServiceSerializer(data = services, many=True)
        return Response(ser_services.data, status=status.HTTP_200_OK)


