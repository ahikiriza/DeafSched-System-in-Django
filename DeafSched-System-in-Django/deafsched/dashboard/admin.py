from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display =Patient.DisplayFields
    search_fields =Patient.SearchableFields
    list_filter =Patient.FilterFields

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display =Doctor.DisplayFields
    search_fields =Doctor.SearchableFields
    
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display =Appointment.DisplayFields
    search_fields =Appointment.SearchableFields
    
@admin.register(CommunicationRequest)
class CommunicationRequestAdmin(admin.ModelAdmin):
    list_display =CommunicationRequest.DisplayFields
    search_fields =CommunicationRequest.SearchableFields
    
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display =Schedule.DisplayFields
    search_fields =Schedule.SearchableFields
    
@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display =Leave.DisplayFields
    search_fields =Leave.SearchableFields