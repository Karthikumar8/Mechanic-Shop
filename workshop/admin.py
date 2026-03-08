from django.contrib import admin
from .models import Mechanic, Customer, Vehicle, WorkOrder

admin.site.register(Mechanic)
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(WorkOrder)
