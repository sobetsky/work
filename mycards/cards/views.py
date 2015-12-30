# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from models import Issues, Cards, Profile, Purchases, Status, Periods
from forms import IssuesForm, ProfileForm
import sqlite3
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
						number = int(str(issue.series) + str(i+1)), 
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
		if not q:
			pass
		else:
			args['cards_serie_filter'] = Cards.objects.filter(
										     series__series__icontains = q)
	
	if request.POST:
		#q = request.POST.get('q_number')
		#args['cards_number_filter'] = Cards.objects.filter(number__icontains = q)
		
		return render_to_response('interface.html', args)
	return render_to_response('interface.html', args)
#___


	
@login_required
def card(request, card_id):
	args = {}
	args.update(csrf(request))
	args['request'] = request
	card = Cards.objects.get(id=card_id)
	args['card'] = card
	new_form = ProfileForm
	args['form'] = new_form
	if request.POST:
		form = ProfileForm(request.POST)
		if form.is_valid():
			p = form.save()
			card.profile = p
			card.save()
		else:
			args['form'] = new_form
			
		return render_to_response('card.html', args)
	return render_to_response('card.html', args)
#___	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#___
