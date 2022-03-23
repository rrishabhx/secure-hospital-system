from django.forms import ModelForm
from django.apps import apps

class CreatePatientForm(ModelForm):
	class Meta:
		model = apps.get_model('hospital', 'Diagnosis')
		fields = ('appointment','doctor', 'patient')

class ViewPatientForm(ModelForm):
	class Meta:
		model = apps.get_model('hospital', 'Diagnosis')
		fields = ('patient','doctor')
        
class ViewPatientRecords(ModelForm):
	class Meta:
		model = apps.get_model('hospital', 'Diagnosis')
		fields = ('patient',)
        
class CreateTransaction(ModelForm):
	class Meta:
		model = apps.get_model('patients', 'Transactions')
		fields = ('patientID','staffId','status','transactionAmount',) 
		readonly_fields = ('staffId','status')


class ViewLabRecords(ModelForm):
	class Meta:
		model = apps.get_model('hospital', 'LabTest')
		fields = ('patient',)