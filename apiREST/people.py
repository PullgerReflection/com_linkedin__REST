from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from pullgerReflection.com_linkedin import models
from pullgerReflection.com_linkedin import api

from pullgerInternalControl.pullgerReflection.REST.logging import logger

from .. import serializers
from .general import CustomPaginator


class PostListView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    queryset = models.People.objects.get_all_persons()

    content = {
        'status': '',
        'message': None,
        'data': None,
    }

    def get(self, request, *args, **kwargs):
        self.serializer_class = serializers.PeopleListSerializer

        try:
            returnResponse = self.list(request, *args, **kwargs)
        except BaseException as e:
            logger.critical(f"Error on executing request [{str(request)}] execute 'self.list': {str(e)}")

            self.content['status'] = 'error'
            self.content['message'] = 'Internal server error.'
            self.content['data'] = None
            statusResp = status.HTTP_500_INTERNAL_SERVER_ERROR

            returnResponse = Response(self.content, status=statusResp)

        return returnResponse

    def post(self, request, *args, **kwargs):
        self.serializer_class = serializers.PeopleModifySerializer
        try:
            returnResponse = self.create(request, *args, **kwargs)
        except BaseException as e:
            logger.critical(f"Error on executing request [{str(request)}] execute 'self.list': {str(e)}")

            self.content['status'] = 'error'
            self.content['message'] = 'Internal server error.'
            self.content['data'] = None
            statusResp = status.HTTP_500_INTERNAL_SERVER_ERROR

            returnResponse = Response(self.content, status=statusResp)

        return returnResponse


class PeopleRetrieveUpdateDeleteView(generics.GenericAPIView,
                                     mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    queryset = models.People.objects.get_all_persons()

    def get(self, request, *args, **kwargs):
        try:
            self.serializer_class = serializers.PeopleListSerializer
            return_response = self.retrieve(request, *args, **kwargs)
        except:
            pass

        return return_response

    def put(self, request, *args, **kwargs):
        self.serializer_class = serializers.PeopleModifySerializer
        return_response = self.update(request, *args, **kwargs)
        return return_response

    def delete(self, request, *args, **kwargs):
        self.serializer_class = serializers.PeopleModifySerializer
        return_response = self.destroy(request, *args, **kwargs)
        return return_response
