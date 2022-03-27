from django import forms
from datetime import datetime
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

class ViewLabRecords(ModelForm):
	class Meta:
		model = apps.get_model('hospital', 'LabTest')
		fields = ('patient',)

