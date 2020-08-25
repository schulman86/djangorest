from django.contrib import admin
from django.urls import path, include
from .views import *
from .models import *

urlpatterns = [
    path('referencelist/', ReferenceListView.as_view()),
   
]