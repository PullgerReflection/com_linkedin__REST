from rest_framework import serializers
from pullgerReflection.com_linkedin import models


class PeopleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.people
        fields = ["uuid", "id", "nick", "first_name", "second_name", "full_name", "url", "discription", "location", "date_small_loaded", "date_full_loaded"]


class PeopleModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.people
        fields = ["id", "nick", "first_name", "second_name", "full_name", "url", "discription", "location", "date_small_loaded", "date_full_loaded"]


class CompaniesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.companies
        fields = '__all__'


class CompaniesModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.companies
        fields = '__all__'
