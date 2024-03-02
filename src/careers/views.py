from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import Career
from .serializers import CareerSerializer


class CareersViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing career instances.

    This ViewSet provides CRUD operations for managing career instances.

    Attributes:
        queryset (QuerySet): The queryset of all career instances.
        serializer_class (Serializer): The serializer class for converting career instances into JSON representations.
    """
    
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

    