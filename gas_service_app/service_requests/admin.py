from django.contrib import admin

# Register your models here.
# service_requests/admin.py
from django.contrib import admin
from .models import ServiceRequest, Customer, CustomerSupportRep

admin.site.register(ServiceRequest)
admin.site.register(Customer)
admin.site.register(CustomerSupportRep)
