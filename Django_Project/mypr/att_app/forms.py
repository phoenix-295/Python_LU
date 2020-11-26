from django import forms
from .models import Master_Data

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class MasterForm(forms.ModelForm):
	class Meta:
		model = Master_Data
		fields = ['name', 'roll_no', 'class_name', 'email1']