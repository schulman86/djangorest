from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
import datetime

class ReferenceListView(generics.ListAPIView):
    serializer_class = ReferenceListViewSerializer
    queryset = Reference.objects.all()

