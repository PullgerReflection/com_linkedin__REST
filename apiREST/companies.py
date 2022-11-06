from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from pullgerReflection.com_linkedin import models
from pullgerReflection.com_linkedin import api

from pullgerInternalControl.pullgerReflection.REST.logging import logger

from .. import serializers
from .general import CustomPaginator


class CompaniesListView(generics.GenericAPIView,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    queryset = models.companies.objects.get_list()

    def get(self, request, *args, **kwargs):
        self.serializer_class = serializers.CompaniesListSerializer
        try:
            returnResponse = self.list(request, *args, **kwargs)
        except BaseException as e:
            pass
        return returnResponse


class CompaniesRetrieveUpdateDeleteView(generics.GenericAPIView,
                                        mixins.RetrieveModelMixin,
                                        mixins.UpdateModelMixin,
                                        mixins.DestroyModelMixin):

    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    queryset = models.companies.objects.get_list()

    def get(self, request, *args, **kwargs):
        try:
            self.serializer_class = serializers.CompaniesListSerializer
            return_response = self.retrieve(request, *args, **kwargs)
        except:
            pass

        return return_response

    def put(self, request, *args, **kwargs):
        self.serializer_class = serializers.CompaniesModifySerializer
        return_response = self.update(request, *args, **kwargs)
        return return_response

    def delete(self, request, *args, **kwargs):
        self.serializer_class = serializers.CompaniesModifySerializer
        return_response = self.destroy(request, *args, **kwargs)
        return return_response
