from rest_framework import serializers
from pullgerReflection.com_linkedin import models


class CompaniesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Companies
        fields = '__all__'


class CompaniesModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Companies
        fields = '__all__'
