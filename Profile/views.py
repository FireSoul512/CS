from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Importar modelo
from Profile.models import Profile, Ciudad, Genero, Ocupacion, Estado, EstadoCivil
# Importar Serializer
from Profile.serializer import ProfileSerializers, CiudadSerializers, GeneroSerializers, OcupacionSerializers, EstadoSerializers, EstadoCivilSerializers

class CiudadList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Ciudad.objects.filter(delete = False)
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GeneroList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Genero.objects.filter(delete = False)
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Ocupacion.objects.filter(delete = False)
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Estado.objects.filter(delete = False)
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCivilList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = EstadoCivil.objects.filter(delete = False)
        serializer = EstadoCivilSerializers(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = EstadoCivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    #Metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Profile.objects.filter(delete = False)
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = ProfileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)