from django import forms
from .models import WorkOrder


class WorkOrderForm(forms.ModelForm):

    class Meta:
        model = WorkOrder
        fields = [
            "description",
            "status",
            "estimated_cost",
            "vehicle",
            "mechanic"
        ]

        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "estimated_cost": forms.NumberInput(attrs={"class": "form-control"}),
            "vehicle": forms.Select(attrs={"class": "form-control"}),
            "mechanic": forms.Select(attrs={"class": "form-control"}),
        }

        