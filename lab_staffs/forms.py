from django import forms
from hospital.models import LabTest

class labTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ('doctor', 'patient', 'diagnosis', 'lab_test_report')