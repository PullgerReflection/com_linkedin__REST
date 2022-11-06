from rest_framework import serializers
from pullgerReflection.com_linkedin import models


class PeopleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.People
        fields = ["uuid", "id", "nick", "first_name", "second_name", "full_name", "url", "description", "location", "date_small_loaded", "date_full_loaded"]


class PeopleModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.People
        fields = ["id", "nick", "first_name", "second_name", "full_name", "url", "description", "location", "date_small_loaded", "date_full_loaded"]
