from django.urls import path
from .views import get_veh_org, get_vehicles_org_sub,get_vehicles_sub_data, fetch_veh_org


urlpatterns = [
    path('api/org',get_veh_org),
    path('get_sub_org/<int:id>',get_vehicles_org_sub),
    path('get_sub_org_data/<int:id>',get_vehicles_sub_data),
    path('',fetch_veh_org)
]

