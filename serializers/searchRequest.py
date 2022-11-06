from rest_framework import serializers
from pullgerReflection.com_linkedin import models


class SearchRequestsModifySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SearchRequests
        fields = '__all__'
