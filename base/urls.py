from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import MyLogoutView

app_name = 'asset_tracker'

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('devices/', views.device_list, name='device_list'),
    path('devices/<int:device_id>/', views.device_detail, name='device_detail'),
    path('devices/<int:device_id>/check_out/', views.check_out_device, name='check_out_device'),
    path('devices/<int:device_id>/check_in/', views.check_in_device, name='check_in_device'),
    path('employees/new/', views.employee_create, name='employee_create'),
    path('', auth_views.LoginView.as_view(template_name='asset_tracker/login.html'), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
