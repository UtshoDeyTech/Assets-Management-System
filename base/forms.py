from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Company, Employee


class CompanySignUpForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=100)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Company
        fields = ['email', 'name']


class EmployeeSignUpForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=100)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['email', 'name', 'company']
