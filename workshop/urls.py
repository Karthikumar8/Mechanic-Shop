from django.urls import path
from .views import (
    dashboard,
    WorkOrderListView,
    WorkOrderCreateView,
    WorkOrderUpdateView,
    WorkOrderDeleteView
)

urlpatterns = [

    # Dashboard
    path('', dashboard, name="dashboard"),

    # WorkOrder CRUD
    path('workorders/', WorkOrderListView.as_view(), name="workorder_list"),
    path('workorders/create/', WorkOrderCreateView.as_view(), name="workorder_create"),
    path('workorders/<int:pk>/update/', WorkOrderUpdateView.as_view(), name="workorder_update"),
    path('workorders/<int:pk>/delete/', WorkOrderDeleteView.as_view(), name="workorder_delete"),

]