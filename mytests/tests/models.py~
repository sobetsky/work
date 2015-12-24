from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Correct(models.Model):
    class Meta():
        db_table = 'corranswer'
        
    answer = models.CharField(max_length = 8)
    def __unicode__(self):
        return self.answer

class QuetionsIntelligence(models.Model):
    class Meta:
        db_table = 'intelligence'

    quetion = models.TextField()
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()    
    correct = models.ForeignKey(Correct)
    def __unicode__(self):
        return self.quetion

class QuetionsPhisical(models.Model):
    class Meta:
        db_table = 'phisical'

    quetion = models.TextField()
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()    
    correct = models.ForeignKey(Correct)

class QuetionsMathematic(models.Model):
    class Meta:
        db_table = 'mathematic'

    quetion = models.TextField()
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()    
    correct = models.ForeignKey(Correct)
    
class TestsList(models.Model):
    class Meta():
        db_table = 'testslist'

    subject = models.CharField(max_length = 80)
    def __unicode__(self):
        return self.subject
    
class TestResult(models.Model):
	class Meta:
		db_table = 'result_test'
		
	user = models.CharField(max_length = 30)   
	date_passing = models.DateTimeField()
	last_question = models.IntegerField()
	correct_answers = models.IntegerField()
	result_passing = models.CharField(max_length = 300)
		
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
