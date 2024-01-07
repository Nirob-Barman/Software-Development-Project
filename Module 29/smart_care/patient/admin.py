from django.contrib import admin
from .models import Patient
# Register your models here.


class PatientModelAdmin(admin.ModelAdmin):
    # list_display = ['get_first_name', 'get_last_name', 'user', 'image', 'mobile_no']

    # def get_first_name(self, obj):
    #     return obj.user.first_name
    
    # def get_last_name(self, obj):
    #     return obj.user.last_name

    list_display = ['first_name', 'last_name', 'user', 'image', 'mobile_no']

    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name


admin.site.register(Patient, PatientModelAdmin)
