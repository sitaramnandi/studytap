from django.contrib import admin
from api.models import student
# Register your models here.
@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display=["id","stname","age"]
# admin.site.register(student,StudentAdmin)
