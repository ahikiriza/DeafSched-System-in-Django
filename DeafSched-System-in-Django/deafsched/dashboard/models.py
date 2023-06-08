from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# Create your models here.
   
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname =models.CharField(max_length=50)
    lastname =models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender =models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob =models.DateField()
    email =models.EmailField(max_length=255, null =True)
    contact_number =models.CharField(max_length=20)
    address =models.CharField(max_length=255, null=True, blank=True)
    
    DisplayFields =['firstname', 'lastname', 'gender','dob','email', 'contact_number', 'address']
    SearchableFields =['firstname', 'lastname', 'gender','dob','email', 'contact_number', 'address']
    FilterFields =['firstname', 'lastname', 'gender', 'contact_number']
    class Meta:
        db_table ='PATIENT'
    

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname =models.CharField(max_length=50)
    lastname =models.CharField(max_length=50)
    SPECIALITIES_CHOICES = (
        ('Otalaryngology', 'Otalaryngology'),
        ('Audiology', 'Audiology'),
        ('Mental Health Services', 'Mental Health Services'),
        ('Speech therapy','Speech therapy'),
        ('General Surgery', 'General Surgery'),
        ('Sign language Interprentation', 'Sign language Interprentation'),
        ('Internal Medicine', 'Internal Medicine')
    )
    specialities =models.CharField(max_length=255, choices=SPECIALITIES_CHOICES)
    email =models.EmailField(max_length=255, null =True)
    contact_number =models.CharField(max_length=20)
    
    DisplayFields =['firstname', 'lastname', 'specialities','email', 'contact_number']
    SearchableFields =['firstname', 'lastname', 'specialities','email', 'contact_number']
    class Meta:
        db_table ='DOCTOR'

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    
    DisplayFields =['patient', 'doctor', 'appointment_date','status']
    SearchableFields =['patient', 'doctor', 'appointment_date','status']
    class Meta:
        db_table ='APPOINTMENT'
    

class CommunicationRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    requested_communication_method = models.CharField(max_length=100)
    request_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    
    DisplayFields =['patient', 'requested_communication_method', 'request_date','status']
    SearchableFields =['patient', 'requested_communication_method', 'request_date','status']
    class Meta:
        db_table ='COMMUNICATION REQUEST'


class Schedule(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    schedule_date =models.DateField()
    timeslot =models.TimeField()
    availability_status = models.CharField(max_length=20)
    
    DisplayFields =['doctor', 'schedule_date', 'timeslot','availability_status']
    SearchableFields =['doctor', 'schedule_date', 'timeslot','availability_status']
    class Meta:
        db_table ='SCHEDULE'

class Leave(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_reason = models.CharField(max_length=100)
    
    DisplayFields =['doctor', 'start_date', 'end_date','leave_reason']
    SearchableFields =['doctor', 'start_date', 'end_date','leave_reason']
    class Meta:
        db_table ='LEAVE'
  

