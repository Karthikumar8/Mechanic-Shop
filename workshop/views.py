from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import WorkOrder
from .forms import WorkOrderForm


# Dashboard View
def dashboard(request):

    total = WorkOrder.objects.count()
    planned = WorkOrder.objects.filter(status="Planned").count()
    progress = WorkOrder.objects.filter(status="In Progress").count()
    completed = WorkOrder.objects.filter(status="Completed").count()

    context = {
        "total": total,
        "planned": planned,
        "progress": progress,
        "completed": completed
    }

    return render(request, "dashboard.html", context)


# WorkOrder List
class WorkOrderListView(ListView):
    model = WorkOrder
    template_name = "workorder_list.html"
    context_object_name = "workorders"


# Create WorkOrder
class WorkOrderCreateView(CreateView):
    model = WorkOrder
    form_class = WorkOrderForm
    template_name = "workorder_form.html"
    success_url = reverse_lazy("workorder_list")


# Update WorkOrder
class WorkOrderUpdateView(UpdateView):
    model = WorkOrder
    form_class = WorkOrderForm
    template_name = "workorder_form.html"
    success_url = reverse_lazy("workorder_list")


# Delete WorkOrder
class WorkOrderDeleteView(DeleteView):
    model = WorkOrder
    template_name = "workorder_confirm_delete.html"
    success_url = reverse_lazy("workorder_list") 