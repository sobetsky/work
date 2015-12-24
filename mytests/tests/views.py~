#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404
from django.core.context_processors import csrf
from models import TestsList, QuetionsIntelligence, QuetionsPhisical, QuetionsMathematic
from django.contrib.auth.decorators import login_required

TL = {
		'Quetions Intelligence': QuetionsIntelligence,
		'Quetions Phisical': QuetionsPhisical,
		'Quetions Mathematic': QuetionsMathematic
	}


def tests(request):
	tests = TestsList.objects.all()
	
	if request.user.is_authenticated():
		username = request.user
	else:
		username =''
		
	return render_to_response('tests.html', locals())
	
#___	
	
@login_required	
def quetions(request, test_id):
	
	test = TestsList.objects.get(id=test_id)
	Quetions = TL[test.subject]
	quetions = Quetions.objects.all()
	request.session['length'] = len(quetions)
	return render_to_response('test.html', locals())
#
@login_required
def testing(request, test_id, quetion_id):
	if quetion_id == '1':
		request.session.set_expiry(3600)
		request.session['count'] = 0
		request.session['open'] = True
		#return HttpResponse('session ok')
		
	args = {}
	args.update(csrf(request))
	
	test = TestsList.objects.get(id=test_id)
	Quetions = TL[test.subject]
	args['quetion'] = Quetions.objects.get(id=quetion_id)
	args['test_id'] = test_id
	args['quetion_id'] = quetion_id
	
	if request.POST and ('open' in request.session):
		ANSWER = request.POST.get('answer', '')
		if not ANSWER:
			args['error'] = 'do not select any answer'
			return render_to_response('testing.html', args)
		
		quetion = args['quetion']
		CORRECT_ANSWER = quetion.correct
		if str(ANSWER) in str(CORRECT_ANSWER):
			request.session['count'] += 1 
			#return HttpResponse(request.session['count'])
		# переходим к следующему волросу	
		quetion_id = int(quetion_id) + 1
		# проверяем конец вопросов
		if quetion_id > request.session['length']:
			return redirect('/test/result/')
		return redirect('/test/testing/%s/%s/' %(test_id, quetion_id))
	return render_to_response('testing.html', args)

#
@login_required	
def result(request):
	L = request.session['length']
	C = request.session['count']
	return render_to_response('result.html', locals())
	
#____
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
