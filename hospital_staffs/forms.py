from django.forms import ModelForm
from django.apps import apps

class CreatePatientForm(ModelForm):
	class Meta:
		model = apps.get_model('patients', 'PatientRecords')
		fields = '__all__'
        
class ViewPatientForm(ModelForm):
	class Meta:
		model = apps.get_model('patients', 'PatientRecords')
		fields = ('patientID','doctorId')
        
class ViewPatientRecords(ModelForm):
	class Meta:
		model = apps.get_model('patients', 'PatientRecords')
		fields = ('patientID',)
        
        
class ViewLabRecords(ModelForm):
	class Meta:
		model = apps.get_model('lab_staffs', 'LabStaffProfile')
		fields = ('patientId',)
        

class CreateTransaction(ModelForm):
	class Meta:
		model = apps.get_model('patients', 'Transactions')
		fields = '__all__'