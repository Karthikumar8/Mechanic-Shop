from rest_framework import serializers
from .models import Mechanic, Customer, Vehicle, WorkOrder


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = ['id', 'name', 'specialty', 'phone']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone']


class VehicleSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'make', 'model', 'year', 'license_plate', 'customer']


class WorkOrderSerializer(serializers.ModelSerializer):

    vehicle = VehicleSerializer(read_only=True)
    mechanic = serializers.StringRelatedField()

    class Meta:
        model = WorkOrder
        fields = [
            'id',
            'description',
            'status',
            'estimated_cost',
            'vehicle',
            'mechanic',
            'created_at',
            'updated_at'
        ]