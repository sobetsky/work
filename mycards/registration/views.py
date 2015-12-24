#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from django.contrib.auth.forms import UserCreationForm

def profile_(request):
	return redirect('/cards/0/')
#___

def registration_(request):
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
			return redirect ('/cards/0/')
		else:
			args['form'] = newuser_form
			
	return render_to_response('registration.html', args)
























	
