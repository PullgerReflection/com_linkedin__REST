from django.urls import path
from . import apiREST

urlpatterns = [
    path('ping', apiREST.Ping.as_view()),
    path('people', apiREST.PostListView.as_view()),
    path('people/<str:pk>', apiREST.PeopleRetrieveUpdateDeleteView.as_view()),
    path('companies', apiREST.CompaniesListView.as_view()),
    path('companies/<str:pk>', apiREST.CompaniesRetrieveUpdateDeleteView.as_view()),
    path('threadtask/ping', apiREST.ThreadTaskPing.as_view()),
    path('threadtask/sendAllTaskForProcessing', apiREST.ThreadTaskSendAllTaskForProcessing.as_view()),
]