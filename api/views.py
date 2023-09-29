from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg

from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer, UpdateCustomerSerializer
from .permissions import CustomPatchPermission


class CustomerViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['last_name']
    permission_classes = [CustomPatchPermission]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateCustomerSerializer
        return CustomerSerializer


    @action(methods=['get'], url_path='age/average', detail=False)
    def average_age(self, request):
        avg_age = self.get_queryset().aggregate(avg_age=Avg('age'))['avg_age']
        return Response({'average_age': round(avg_age, 1)})
