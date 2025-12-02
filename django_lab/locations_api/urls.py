from django.urls import path
from . import views

urlpatterns = [
    path('api/company', views.CompanyList.as_view(), name='company_list'), # api/company will be routed to the CompanyList view for handling
    path('api/company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'), # api/company will be routed to the CompanyDetail view for handling
    path('api/location', views.LocationList.as_view(), name='location_list'), # api/location will be routed to the LocationList view for handling
    path('api/location/<int:pk>', views.LocationDetail.as_view(), name='location_detail'), # api/location will be routed to the LocationDetail view for handling
]