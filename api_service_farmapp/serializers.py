from rest_framework import serializers
from .models import FarmerDetails

class FarmerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerDetails
        fields = '__all__'
