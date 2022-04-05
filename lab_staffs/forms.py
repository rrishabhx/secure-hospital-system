from django.forms import ModelForm, forms
from hospital.models import LabTest, Diagnosis


class LabTestCreateForm(ModelForm):
    class Meta:
        model = LabTest
        fields = ('diagnosis', 'lab_test_report')

    def __init__(self, *args, **kwargs):
        super(LabTestCreateForm, self).__init__(*args, **kwargs)
        self.fields['diagnosis'].queryset = Diagnosis.objects.filter(lab_test_status__isnull=True,
                                                                     lab_tests_recommended__isnull=False)

    def clean_diagnosis(self):
        diagnosis = self.cleaned_data['diagnosis']
        exist = LabTest.objects.filter(diagnosis=diagnosis).exists()

        if exist:
            raise forms.ValidationError('lab test already exist')

        return diagnosis


class LabTestUpdateForm(ModelForm):
    class Meta:
        model = LabTest
        fields = ['lab_test_report']
