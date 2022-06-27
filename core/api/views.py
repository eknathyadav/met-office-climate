from django.shortcuts import render

# Create your views here.
from functools import partial
from core.models import Region, Parameter, YearTemperature, MonthTemperature
from .serializers import RegionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def regions_list(request):
    if request.method == 'GET':
        regions = Region.objects.all()
        serializers = RegionSerializer(regions, many=True,
                                       context={"parameter": "ALL"})
        return Response(serializers.data)


@api_view(['GET'])
def get_region(request, region_name):
    if request.method == 'GET':
        regions = Region.objects.filter(regionName=region_name)
        serializers = RegionSerializer(regions, many=True,
                                       context={"parameter": "ALL"})
        return Response(serializers.data)


@api_view(['GET'])
def get_regions_parameter(request, parameter_name):
    if request.method == 'GET':
        regions = Region.objects.all()
        serializers = RegionSerializer(regions, many=True,
                                       context={"parameter": parameter_name})
        return Response(serializers.data)


@api_view(['GET'])
def get_region_parameter(request, region_name, parameter_name):
    if request.method == 'GET':
        regions = Region.objects.filter(regionName=region_name)
        serializers = RegionSerializer(regions, many=True,
                                       context={"parameter": parameter_name})
        return Response(serializers.data)
