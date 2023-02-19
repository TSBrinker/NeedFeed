from rest_framework import serializers
from .models import Primary_Category

class PrimaryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Primary_Category
        fields = ['id', 'name', 'description']