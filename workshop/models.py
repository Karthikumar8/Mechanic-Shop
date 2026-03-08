from django.db import models


class Mechanic(models.Model):
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=20, unique=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='vehicles'
    )

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"


class WorkOrder(models.Model):

    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    mechanic = models.ForeignKey(
        Mechanic,
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"WorkOrder #{self.id} - {self.status}"
