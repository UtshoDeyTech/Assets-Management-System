from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Company, Employee, Device
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView


@login_required
def home(request):
    return render(request, 'asset_tracker/home.html')


@login_required
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'asset_tracker/company_list.html', {'companies': companies})


@login_required
def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'asset_tracker/company_detail.html', {'company': company})


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'asset_tracker/employee_list.html', {'employees': employees})

@login_required
def employee_create(request):
    if request.method == 'POST':
        # create a new employee object with the form data
        employee = Employee(name=request.POST['name'], company_id=request.POST['company'])
        employee.save()
        messages.success(request, 'New employee added.')
        return redirect('asset_tracker:employee_list')
    else:
        companies = Company.objects.all()
        return render(request, 'asset_tracker/employee_create.html', {'companies': companies})


@login_required
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'asset_tracker/employee_detail.html', {'employee': employee})


@login_required
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'asset_tracker/device_list.html', {'devices': devices})


@login_required
def device_detail(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    return render(request, 'asset_tracker/device_detail.html', {'device': device})


@login_required
def check_out_device(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee = get_object_or_404(Employee, pk=employee_id)
        device.checked_out_by = employee
        device.checked_out_date = timezone.now()
        device.status = 'checked out'
        device.save()
        messages.success(request, f'{device.name} was checked out by {employee.name}.')
        return redirect('asset_tracker:device_detail', device_id=device.id)
    else:
        employees = Employee.objects.filter(company=device.company)
        return render(request, 'asset_tracker/check_out_device.html', {'device': device, 'employees': employees})


@login_required
def check_in_device(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    device.checked_out_by = None
    device.checked_out_date = None
    device.checked_in_date = timezone.now()
    device.status = 'available'
    device.save()
    messages.success(request, f'{device.name} was checked in.')
    return redirect('asset_tracker:device_detail', device_id=device.id)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('asset_tracker:home')
    else:
        form = UserCreationForm()
    return render(request, 'asset_tracker/signup.html', {'form': form})




class MyLogoutView(LogoutView):
    template_name = 'my_logout.html'


class HomePageView(TemplateView):
    template_name = 'asset_tracker/home.html'

class MyLogoutView(LogoutView):
    template_name = 'my_logout.html'