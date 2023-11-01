from apps.vehicle_admin.views import VehicleListView
from django.urls import path

model_name = 'vehicle'
model_url_name = model_name.replace('-', '_')

urlpatterns = [
    path(
        'vehicle/list/', 
        VehicleListView.as_view(),
        name=f'{model_name}_list'
    ),
]
