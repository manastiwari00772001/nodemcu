from django import forms

class SaveForm(forms.Form):
    UIDresult = forms.CharField(label='UIDresult', max_length=200)