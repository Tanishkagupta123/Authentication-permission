from django.shortcuts import render

# Create your views here.
from .models import Student
from .serializers import StuSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework import viewsets

# class all_data(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Student.objects.all()
#     serializer_class = StuSerializer

# class data(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StuSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Student.objects.all()
    serializer_class = StuSerializer
