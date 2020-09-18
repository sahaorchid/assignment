from rest_framework import viewsets

from REST_Assignment.projectapp.models import Customers
from . import serializers
class CustomersViewset(viewsets.ModelViewSet):
    queryset = Customers.objects.all()


    serializer_class = serializers.CustomersSerializer