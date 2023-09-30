from rest_framework import serializers
from . import models


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id', 'last_name']


class UpdateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['last_name', 'age']

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be greater than 18")
        return value
