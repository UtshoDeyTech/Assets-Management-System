from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Device(models.Model):
    CONDITION_CHOICES = [
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='available')
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='checked_out_devices')
    checked_out_date = models.DateTimeField(null=True, blank=True)
    checked_in_date = models.DateTimeField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
