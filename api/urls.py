from django.urls import path
from .views import CompanyList, CompanyDetail, EmployeeList, EmployeeDetail, DeviceList, DeviceDetail

urlpatterns = [
    path('companies/', CompanyList.as_view(), name='company_list'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('devices/', DeviceList.as_view(), name='device_list'),
    path('devices/<int:pk>/', DeviceDetail.as_view(), name='device_detail'),
]
