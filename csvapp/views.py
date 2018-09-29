from django.shortcuts import render
from models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from rest_framework import status
from serializers import *
# Create your views here.


class CSVview(ModelViewSet):

	queryset=item.objects.all()
	serializer_class=itemSerializer
