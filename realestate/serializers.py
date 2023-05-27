from rest_framework import serializers
from .models import RealEstate


class RealEstateSerializer(serializers.ModelSerializer):
    """
    This is the Serializers class for Realestate
    It's serialize all fields from database.
    """
    class Meta:
        model = RealEstate
        fields = '__all__'
