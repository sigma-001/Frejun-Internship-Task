from django.urls import path
from .views import InitiateCallView, CallReportView, CallRecordView



urlpatterns = [
    path('initiate-call/',InitiateCallView.as_view()),
    path('call-report/',CallReportView.as_view()),
    path('call-record/<int:pk>/',CallRecordView.as_view()),
]