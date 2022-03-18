from django.contrib import admin

from hospital.models import Appointment, Diagnosis, LabTest

admin.site.register(Appointment)
admin.site.register(Diagnosis)
admin.site.register(LabTest)
