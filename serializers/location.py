from rest_framework import serializers
from pullgerReflection.com_linkedin import models


class LocationsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Locations
        fields = '__all__'
