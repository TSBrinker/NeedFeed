from rest_framework import serializers
from .models import Secondary_Category

class SecondaryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Secondary_Category
        fields = ['id', 'name', 'description']