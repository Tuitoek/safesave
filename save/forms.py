from django import forms
from .models import *

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','email','name']


class  FinanceForm(forms.ModelForm):
    class Meta:
        model = Finance
        fields = ['user','expenses','salaryearned','savings','months']

class SavingsForm(forms.ModelForm):
    class Meta:
        model = SavingPlan
        fields = ['amount','month']
