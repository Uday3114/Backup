from django import forms
from .models import BankForm


'''class AccRegistration(forms.Form):
    # TODO: Define form fields here
    NAME = forms.CharField()
	AGE = forms.IntegerField()
	DOB = forms.DateField()
	ADDRESS = forms.CharField()
	ACCTYPE = forms.CharField()
	BRANCH = forms.CharField()
	EMAIL = forms.EmailField()
	AADHARNO = forms.IntegerField()'''

class AccRegistration(forms.ModelForm):
    # TODO: Define form fields here

    class Meta:
    	model = BankForm
    	fields = '__all__'
    

