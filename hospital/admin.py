from django.contrib import admin

from hospital.models import Appointment, Diagnosis, LabTest, InsurancePolicy, InsuredPatient, InsuranceClaim

admin.site.register(Appointment)
admin.site.register(Diagnosis)
admin.site.register(LabTest)
admin.site.register(InsurancePolicy)
admin.site.register(InsuredPatient)
admin.site.register(InsuranceClaim)
