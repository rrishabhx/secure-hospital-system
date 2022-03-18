from django.contrib import admin

from patients.models import PatientProfile, MedicalInsurance

admin.site.register(PatientProfile)
admin.site.register(MedicalInsurance)
