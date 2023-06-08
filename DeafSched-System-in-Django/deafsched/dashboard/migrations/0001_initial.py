# Generated by Django 4.2.2 on 2023-06-08 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('specialities', models.CharField(choices=[('Otalaryngology', 'Otalaryngology'), ('Audiology', 'Audiology'), ('Mental Health Services', 'Mental Health Services'), ('Speech therapy', 'Speech therapy'), ('General Surgery', 'General Surgery'), ('Sign language Interprentation', 'Sign language Interprentation'), ('Internal Medicine', 'Internal Medicine')], max_length=255)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('contact_number', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'DOCTOR',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_date', models.DateField()),
                ('timeslot', models.TimeField()),
                ('availability_status', models.CharField(max_length=20)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashboard.doctor')),
            ],
            options={
                'db_table': 'SCHEDULE',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=255, null=True)),
                ('contact_number', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'PATIENT',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('leave_reason', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.doctor')),
            ],
            options={
                'db_table': 'LEAVE',
            },
        ),
        migrations.CreateModel(
            name='CommunicationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_communication_method', models.CharField(max_length=100)),
                ('request_date', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.patient')),
            ],
            options={
                'db_table': 'COMMUNICATION REQUEST',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.patient')),
            ],
            options={
                'db_table': 'APPOINTMENT',
            },
        ),
    ]