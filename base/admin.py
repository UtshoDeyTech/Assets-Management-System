from django.contrib import admin
from .models import Company, Employee, Device


class EmployeeInline(admin.TabularInline):
    model = Employee


class DeviceInline(admin.TabularInline):
    model = Device


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline, DeviceInline]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    list_filter = ('company',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'condition', 'checked_out_by', 'checked_out_date', 'checked_in_date', 'company')
    list_filter = ('status', 'condition', 'company')
    search_fields = ('name', 'checked_out_by__name', 'company__name')
