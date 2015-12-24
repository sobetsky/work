from __future__ import unicode_literals

from django.db import models
import datetime





# Table for issues and them conditions
'''
date_of_approval, series, period of time, quantity '''
class Issues(models.Model):
    class Meta():
        db_table = 'issues'
        
    now_=datetime.datetime.now()
    date_of_approval = models.DateTimeField(default = now_)
    
    series = models.IntegerField(default = 1000)
    period = models.ForeignKey('Periods')
    quantity = models.IntegerField()
    #def __unicode__(self):
    #    return self.date_of_approval
        
        
# Table all cards
''' 
date_issue, date_activate, date_end_activate, series, number, status'''
class Cards(models.Model):
    class Meta():
        db_table = 'cards'
    now_=datetime.datetime.now()    
    date_issue = models.DateTimeField(default = now_)
    date_activate = models.DateTimeField(blank=True, null=True)
    date_end_activate = models.DateTimeField(blank=True, null=True)
    series = models.ForeignKey(Issues)
    number = models.IntegerField(default = 0)
    status = models.ForeignKey('Status')
    profile = models.ForeignKey('Profile', blank=True, null=True)
    purchases = models.ManyToManyField('Purchases', blank=True, null=True)
    #def __unicode__(self):
    #    return self.series

# Table Profile
'''
  '''
class Profile(models.Model):
    class Meta():
        db_table = 'profile'
        
    date_creation = models.DateTimeField()    
    first_name = models.CharField(max_length = 30)
    second_name = models.CharField(max_length = 30)
	#def __unicode__(self):
	#	return '%s %s'%(self.first_name, self.second_name)
        
          
# Table purchases associated with the card
class Purchases(models.Model):
    class Meta():
        db_table = 'purchases'
    date_purcheses = models.DateTimeField()
    summ_purcheses = models.DecimalField(max_digits=11, decimal_places=2)
    place_purcheses = models.CharField(max_length = 100)
    purcheses = models.CharField(max_length = 100)
	#def __unicode__(self):
	#	return self.status

# Table status
''' 
active, no active, expired '''
class Status(models.Model):
    class Meta():
        db_table = 'status'
        
    status = models.CharField(max_length = 10)
    def __unicode__(self):
        return self.status


# Table period of time (1m, 3m, 6m, 1Y)  ( %Y %m %d %H:%i)
''' 1Y 6m 3m 1m '''
class Periods(models.Model):
    class Meta():
        db_table = 'period'
        
    period = models.CharField(max_length = 6)
    def __unicode__(self):
        return self.period


