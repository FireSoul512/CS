from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Profile.views import ProfileList, CiudadList, GeneroList, OcupacionList, EstadoList, EstadoCivilList

urlpatterns = [
    re_path(r'Profile/$', ProfileList.as_view()),
    re_path(r'Ciudad/$', CiudadList.as_view()),
    re_path(r'Genero/$', GeneroList.as_view()),
    re_path(r'Ocupacion/$', OcupacionList.as_view()),
    re_path(r'Estado/$', EstadoList.as_view()),
    re_path(r'EstadoCivil/$', EstadoCivilList.as_view()),
]