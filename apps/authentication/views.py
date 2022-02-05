from django.contrib import messages
from .models import MyUser as User
from django.contrib.auth import authenticate, login, logout  # add this
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import NewUserForm, LoginForm


@login_required
def home_page(request):
	context = {
		'title': 'This is a title'
	}
	return render(request=request, template_name='authentication/home.html', context=context)


def register_request(request):
	if request.user.is_authenticated:
		return redirect('homepage')
	else: 
		if request.method == "POST":
			form = NewUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				login(request, user)
				messages.success(request, "Registration successful." )
				return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
		form = NewUserForm()
	
		context = {
			"pagename": 'Registration',
			"form":form, 
			
		}
	return render (request=request, template_name="authentication/register.html", context=context)


def login_request(request):
	if request.method == "POST":
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = LoginForm()
	context = {"pagename": "Login","login_form":form}
	return render(request=request, template_name="authentication/login.html", context=context)


def logout_request(request):
	logout(request)
	redirect('login')
	return render(request, 'authentication/logout.html')

@login_required
def profile(request):
	profile = request.user.profile
	context = {
		"pagename": "Profile",
		'profile': profile
	}
	return render(request, 'authentication/profile.html', context)
