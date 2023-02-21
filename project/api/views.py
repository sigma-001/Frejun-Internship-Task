from rest_framework.generics import *
from .models import CallRecord
from .serializers import CallRecordSerializer
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


# View for Creating the Call
class InitiateCallView(CreateAPIView):
    
    serializer_class = CallRecordSerializer
    

# Creating the Custom Pagination class with custom page_size
class CustomPagination(PageNumberPagination):
    
    page_size = 10


# View for getting the list of records associated with a number
class CallReportView(ListAPIView):
    
    serializer_class = CallRecordSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        phone = self.request.GET.get('phone')
        return CallRecord.objects.filter(Q(from_number = phone) | Q(to_number = phone))
    

# View for updating or deleting a particular call record
# One can't modify the start_time field

class CallRecordView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = CallRecordSerializer
    queryset = CallRecord.objects.all()
    
    