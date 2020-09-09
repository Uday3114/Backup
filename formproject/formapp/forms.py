from django import forms

class StudentRegistration(forms.Form):
    # TODO: Define form fields here
    NAME = forms.CharField()
    MARKS = forms.IntegerField()
