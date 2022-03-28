from django.forms import ModelForm, forms
from hospital.models import LabTest

class labTestForm(ModelForm):
    class Meta:
        model = LabTest
        fields = ('doctor', 'patient', 'diagnosis', 'lab_test_report')


    def clean_diagnosis(self):
        diagnosis = self.cleaned_data['diagnosis']
        patients = self.cleaned_data['patient']
        exist = LabTest.objects.filter(diagnosis = diagnosis).exists()

        if exist:
            raise forms.ValidationError('lab test already exist')
        elif diagnosis.patient.user_id != patients.user_id:
            raise forms.ValidationError('Please select the matched diagnosis')
        return diagnosis

class labTestUpdateForm(ModelForm):
    class Meta:
        model = LabTest
        fields = ('doctor', 'patient', 'diagnosis', 'lab_test_report')