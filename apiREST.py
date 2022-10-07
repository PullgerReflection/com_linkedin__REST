from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from pullgerMultiSessionManager import api
from rest_framework.pagination import PageNumberPagination
from . import serializers
from pullgerReflection.com_linkedin import models
from pullgerLogin.pullgerReflection.REST import logger

loggerName = 'pullgerReflection.com_linkedin.REST'


class CustomPaginator(PageNumberPagination):
    page_size = 5
    max_page_size = 10
    page_query_param = "page"
    page_size_query_param = "limit"

    def get_paginated_response(self, data):
        return Response({
            'status': 'success',
            'data': {
                'count': self.page.paginator.count,
                'page_current': self.page.number,
                'page_max': self.page.paginator.num_pages,
                'page_limit': self.page.paginator.per_page,
                'posts': data
            },
            'message': ''
        })


class Ping(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        content = {'message': 'Pong: ' + loggerName}
        # time.sleep(1)
        return Response(content)


class CompaniesListView(generics.GenericAPIView,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    queryset = models.companies.objects.get_list()

    def get(self, request, *args, **kwargs):
        self.serializer_class = serializers.PeopleListSerializer
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
    queryset = models.people.objects.getAllPersons()

    def get(self, request, *args, **kwargs):
        try:
            self.serializer_class = serializers.PeopleListSerializer
            returnResponce = self.retrieve(request, *args, **kwargs)
        except:
            pass

        return returnResponce

    def put(self, request, *args, **kwargs):
        self.serializer_class = serializers.PeopleModifySerializer
        returnResponce = self.update(request, *args, **kwargs)
        return returnResponce

    def delete(self, request, *args, **kwargs):
        self.serializer_class = serializers.PeopleModifySerializer
        returnResponce = self.destroy(request, *args, **kwargs)
        return returnResponce



class PostListView(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    queryset = models.people.objects.getAllPersons()

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
    queryset = models.people.objects.getAllPersons()

    def get(self, request, *args, **kwargs):
        try:
            self.serializer_class = serializers.PeopleListSerializer
            returnResponce = self.retrieve(request, *args, **kwargs)
        except:
            pass

        return returnResponce

    def put(self, request, *args, **kwargs):
        self.serializer_class = serializers.PeopleModifySerializer
        returnResponce = self.update(request, *args, **kwargs)
        return returnResponce

    def delete(self, request, *args, **kwargs):
        self.serializer_class = serializers.PeopleModifySerializer
        returnResponce = self.destroy(request, *args, **kwargs)
        return returnResponce


class threadTask_Ping(APIView):
    permission_classes = (AllowAny,)
    http_method_names = ('get')

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
                msgPrivat=f"{str(e)}",
                msgPublic="Internal server error."
            )
            content['message'] = 'Pong: Thread Task'
            content['error'] = logRecord.msgPublic
            statusResponse = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            content['message'] = 'Pong: Thread Task'
            statusResponse = status.HTTP_200_OK

        return Response(content, status=statusResponse)


class ThreadTask_SendAllTaskForProcessing(APIView):
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
            api_TT.send_task_for_processing()
        except BaseException as e:
            logRecord = logger.info(
                msgPrivat=f"{str(e)}",
                msgPublic="Internal server error."
            )
            content['message'] = 'Pong: Thread Task'
            content['error'] = logRecord.msgPublic
            statusResponse = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            content['message'] = 'Thread Task sanded for processing.'
            statusResponse = status.HTTP_200_OK

        return Response(content, status=statusResponse)
