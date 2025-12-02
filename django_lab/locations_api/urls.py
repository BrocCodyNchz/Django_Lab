from django.urls import path
from . import views

urlpatterns = [
    path('api/locations', views.LocationsList.as_view(), name='locations_list'), # api/location will be routed to the LocationList view for handling
    path('api/locations/<int:pk>', views.LocationsDetail.as_view(), name='locations_detail'), # api/location will be routed to the LocationDetail view for handling
]