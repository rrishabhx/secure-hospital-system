from django.forms import ModelForm
from django.apps import apps

class CreatePatientForm(ModelForm):
	class Meta:
		model = apps.get_model('hospital', 'Diagnosis')
		fields = ('appointment',)

class ViewPatientForm(ModelForm):
	class Meta:
		model = apps.get_model('hospital', 'Diagnosis')
		fields = ('patient',)
        
class ViewPatientRecords(ModelForm):
	class Meta:
		model = apps.get_model('hospital', 'Diagnosis')
		fields = ('patient',)
        
class CreateTransaction(ModelForm):
	class Meta:
		model = apps.get_model('hospital', 'Transaction')
		fields = ('patient','diagnosis', 'amount')


class ViewLabRecords(ModelForm):
	class Meta:
		model = apps.get_model('hospital', 'LabTest')
		fields = ('patient',)