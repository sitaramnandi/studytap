from django.contrib import admin
from myapp.models import Order
# Register your models here.
# class TaskAdmin(admin.ModelAdmin):
#     list_display=["title","description","status"]
admin.site.register(Order)