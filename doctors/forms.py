from django import forms
from django.forms import ModelForm
from django.apps import apps

class ProfileForm(forms.Form):
    username = forms.CharField(
        label='Username', max_length=100, required=False, disabled=True)
    email = forms.CharField(label='Email', max_length=100,
                            required=False, disabled=True)
    address = forms.CharField(label='Address', max_length=100, required=False)
    insurance = forms.CharField(
        label='Insurance', max_length=100, required=False)


class UpdatePatientForm(ModelForm):
    class Meta:
        model = apps.get_model('hospital', 'Diagnosis')
        fields = ('patient',)
    def __init__(self, plist, *args, **kwargs):
        super(UpdatePatientForm, self).__init__(*args, **kwargs)
        pmodel = apps.get_model('patients', 'PatientProfile')
        self.fields['patient'].queryset = pmodel.objects.filter(pk__in = plist)


class ViewLabRecords(ModelForm):
    class Meta:
        model = apps.get_model('hospital', 'LabTest')
        fields = ('patient',)
