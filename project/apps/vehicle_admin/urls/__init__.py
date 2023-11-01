from django.urls import path
from django.views.generic import TemplateView
from .vehicle import urlpatterns as vehicle_urls

urlpatterns = [
    path('', TemplateView.as_view(template_name='vehicle_admin/home/index.html'), name='logout'),
]

urlpatterns += (
    vehicle_urls
)
