from rest_framework import serializers
from .models import Reference

class ReferenceListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'