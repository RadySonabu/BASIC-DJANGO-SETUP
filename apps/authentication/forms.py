from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from apps.authentication.models import MyUser

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
	contact = forms.CharField()
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput,)
	
	class Meta:
		model = MyUser
		fields = ("first_name","last_name","email", "gender", "contact","date_of_birth","password1")
		
	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class LoginForm(AuthenticationForm):
	username = UsernameField(label='Email',widget=TextInput(attrs={'class':'validate','placeholder': 'Email'}))
	password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
