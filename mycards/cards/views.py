# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from models import Issues, Cards, Profile, Purchases, Status, Periods
from forms import IssuesForm

def page_0(request):

	return render_to_response('page_0.html', locals())
#___
	
@login_required
def generator(request):
	args = {}
	args.update(csrf(request))
	args['request'] = request
	new_form = IssuesForm
	args['form'] = new_form
	args['issues'] = Issues.objects.all()
	if request.POST:
		form = IssuesForm(request.POST)
		if form.is_valid():
			form.save()
			for i in range(int(request.POST['quantity'])):
				issue = Issues.objects.get(series = request.POST['series'])
				p = Cards(
						series = issue,
						number = i, 
						status = Status.objects.get(status='no active')
					)
				p.save()
			return render_to_response('generator.html', args)
		else:
			args['form'] = new_form
		
		
	return render_to_response('generator.html', args)
#___	

@login_required
def interface(request):
	args = {}
	args['request'] = request
	args.update(csrf(request))
	
	if 'q_series' in request.POST:
		q = request.POST.get('q_series')
		args['cards_serie_filter'] = Cards.objects.filter(series__series__icontains = q)
	if 'q_number' in request.POST:
		q = request.POST.get('q_number')
		args['cards_number_filter'] = Cards.objects.filter(number__icontains = q)
		args['q'] = 'OK'
		return render_to_response('interface.html', args)
	return render_to_response('interface.html', args)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#___
