from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment, Patient, Doctor
# Create your views here.

@login_required
def patient_dashboard(request):
    patient = request.user.patient
    upcoming_appointments = Appointment.objects.filter(patient=patient, status='upcoming')
    past_appointments = Appointment.objects.filter(patient=patient, status='past')
    context = {
        'upcoming_appointments': upcoming_appointments,
        'past_appointments': past_appointments,
        'patient': patient,
    }
    return render(request, 'patient_dashboard.html', context)

@login_required
def doctor_dashboard(request):
    doctor = request.user.doctor
    schedule = doctor.schedule
    upcoming_appointments = Appointment.objects.filter(doctor=doctor, status='upcoming')
    context = {
        'schedule': schedule,
        'upcoming_appointments': upcoming_appointments,
        'doctor': doctor,
    }
    return render(request, 'doctor_dashboard.html', context)

@login_required
def admin_dashboard(request):
    # Retrieve necessary data for the admin dashboard
    appointment_stats = Appointment.objects.all().count()
    doctor_profiles = Doctor.objects.all()
    patient_profiles = Patient.objects.all()
    leaves = Leave.objects.all()
    communication_requests = CommunicationRequest.objects.all()

    context = {
        'appointment_stats': appointment_stats,
        'doctor_profiles': doctor_profiles,
        'patient_profiles': patient_profiles,
        'leaves': leaves,
        'communication_requests': communication_requests,
    }
    return render(request, 'admin_dashboard.html', context)
