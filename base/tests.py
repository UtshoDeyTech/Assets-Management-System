from django.test import TestCase, Client
from django.urls import reverse
from .models import Company, Employee, Device
from django.utils import timezone
from django.contrib.auth.models import User


class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('asset_tracker:home')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.company = Company.objects.create(name='Test Company')
        self.employee = Employee.objects.create(name='Test Employee', company=self.company)
        self.device = Device.objects.create(name='Test Device', company=self.company, assigned_to=self.employee)

    def test_home_view_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'asset_tracker/home.html')

    def test_home_view_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('asset_tracker:login')+'?next='+self.url)

    def tearDown(self):
        self.user.delete()
        self.company.delete()
        self.employee.delete()
        self.device.delete()
