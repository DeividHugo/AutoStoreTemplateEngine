from django.views.generic import ListView, UpdateView, CreateView
from apps.vehicle_market.models import Vehicle


class VehicleListView(ListView):
    model = Vehicle
    context_object_name = 'company_adress'
    template_name = 'vehicle_admin/model_templates/vehicle/list.html'
