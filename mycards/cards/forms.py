from django import forms
from django.forms import ModelForm
from models import Issues, Cards, Profile, Purchases 

class IssuesForm(ModelForm):
	class Meta:
		model = Issues
		fields = ['date_of_approval', 'series', 'period', 'quantity']
	
	#date_of_approval = forms.DateTimeField()
	

