from django.forms import ModelForm
from django.apps import apps
from django.db.models import Q

from hospital.models import Appointment


class CreatePatientForm(ModelForm):
    class Meta:
        model = apps.get_model('hospital', 'Diagnosis')
        fields = ('appointment',)

    def __init__(self, ids, *args, **kwargs):
        super(CreatePatientForm, self).__init__(*args, **kwargs)
        self.fields['appointment'].queryset = Appointment.objects.filter(Q(status=True) & ~Q(id__in=ids))


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
        fields = ('patient', 'diagnosis', 'amount')


class ViewLabRecords(ModelForm):
    class Meta:
        model = apps.get_model('hospital', 'LabTest')
        fields = ('patient',)


class ViewAppointment(ModelForm):
    class Meta:
        model = apps.get_model('hospital', 'Appointment')
        fields = ('doctor',)
