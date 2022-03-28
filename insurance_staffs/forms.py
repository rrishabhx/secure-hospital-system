from django import forms

from hospital.models import InsurancePolicy


class InsurancePolicyForm(forms.ModelForm):
    class Meta:
        model = InsurancePolicy
        fields = ('name', 'max_amount')
