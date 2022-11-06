from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from pullgerReflection.com_linkedin import models
from pullgerReflection.com_linkedin import api

from pullgerInternalControl.pullgerReflection.REST.logging import logger

from .. import serializers
from .general import CustomPaginator


class ThreadTaskPing(APIView):
    permission_classes = (AllowAny, )
    http_method_names = ('get',)

    # serializer_class
    # queryset

    def get(self, request):

        content = {
            'message': None,
            'error': None
        }

        try:
            from pullgerReflection import com_linkedin__TT
        except BaseException as e:
            logRecord = logger.info(
                msgt=f"{str(e)}",
                msg_public="Internal server error."
            )
            content['message'] = 'Pong: Thread Task'
            content['error'] = logRecord.msg_public
            statusResponse = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            content['message'] = 'Pong: Thread Task'
            statusResponse = status.HTTP_200_OK

        return Response(content, status=statusResponse)


class ThreadTaskSendAllTaskForProcessing(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = "post"

    # serializer_class
    # queryset

    def post(self, request):
        content = {
            'message': None,
        }

        try:
            from pullgerReflection.com_linkedin__TT import api as api_TT
            api_TT.send_all_task_for_processing()
        except BaseException as e:
            logRecord = logger.info(
                msg_=f"{str(e)}",
                msg_public="Internal server error."
            )
            content['message'] = 'Pong: Thread Task'
            content['error'] = logRecord.msg_public
            statusResponse = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            content['message'] = 'Thread Task sanded for processing.'
            statusResponse = status.HTTP_200_OK

        return Response(content, status=statusResponse)
