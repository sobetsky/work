
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def register_(request):
	
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username = newuser_form.cleaned_data['username'],
										 password = newuser_form.cleaned_data['password2'])
			auth.login(request, newuser)
			return redirect ('/test/all/')
		else:
			args['form'] = newuser_form

	return render_to_response('register.html', args)
#___
	
def profile(request):
	return redirect('/test/all/')
