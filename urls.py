from django.urls import path
from . import apiREST

urlpatterns = [
    path('ping', apiREST.Ping.as_view()),
    path('people', apiREST.PostListView.as_view()),
    path('people/<str:pk>', apiREST.PeopleRetriveUpdateDeleteView.as_view()),
    path('companies', apiREST.CompaniesListView.as_view()),
    path('companies/<str:pk>', apiREST.CompaniesRetriveUpdateDeleteView.as_view()),
    path('threadtask/ping', apiREST.threadTask_Ping.as_view()),
    path('threadtask/sendAllTaskForProcessing', apiREST.ThreadTask_SendAllTaskForProcessing.as_view()),
]