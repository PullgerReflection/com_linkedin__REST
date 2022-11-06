from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from pullgerReflection.com_linkedin import models
from pullgerReflection.com_linkedin import api

from pullgerInternalControl.pullgerReflection.REST.logging import logger

from .. import serializers
from .general import CustomPaginator


class SearchRequestsView(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    queryset = models.SearchRequests.objects.all()

    content = {
        'status': '',
        'message': None,
        'data': None,
    }

    def get(self, request, *args, **kwargs):
        self.serializer_class = serializers.SearchRequestsModifySerializer

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
        content = {
            'message': None,
        }

        # self.serializer_class = serializers.SearchRequestsModifySerializer
        try:
            returnResponse = api.add_people_search(**request.data)
        except BaseException as e:
            logRecord = logger.info(
                msg_=f"{str(e)}",
                msg_public="Internal server error."
            )
            content['message'] = 'Pong: Thread Task'
            content['error'] = logRecord.msg_public
            statusResponse = status.HTTP_500_INTERNAL_SERVER_ERROR

            logger.critical(f"Error on executing request [{str(request)}] execute 'self.list': {str(e)}")
        else:
            content['message'] = 'Thread Task sanded for processing.'
            statusResponse = status.HTTP_201_CREATED

        return Response(content, status=statusResponse)


class SearchRequestsRGUD(generics.GenericAPIView,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    queryset = models.SearchRequests.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            self.serializer_class = serializers.PeopleListSerializer
            return_response = self.retrieve(request, *args, **kwargs)
        except:
            pass

        return return_response

    def put(self, request, *args, **kwargs):
        self.serializer_class = serializers.SearchRequestsModifySerializer
        return_response = self.update(request, *args, **kwargs)
        return return_response

    def delete(self, request, *args, **kwargs):
        self.serializer_class = serializers.PeopleModifySerializer
        return_response = self.destroy(request, *args, **kwargs)
        return return_response
