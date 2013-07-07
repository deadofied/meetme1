from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

 
class Profile(models.Model):
	user = models.OneToOneField(User)	
	location = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	interests = models.TextField()
	active = models.BooleanField(default=True)
	year = models.CharField(max_length=10)
	created = models.DateTimeField(auto_now_add=True)
 
	class Meta:
		ordering = ['-created']
 
	def __unicode__(self):
		return u'%s' % self.user.username
 
	def get_absolute_url(self):
 		return reverse('app.views.profile', args=[self.user.username])

def create_profile(sender, instance, created, **kwargs):  
	if created:  
		profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User) 

class Question(models.Model):
	slug = models.SlugField(unique=True, max_length=255)
	body = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return self.body
 
	class Meta:
		ordering = ['-created']


class Answer(models.Model):
	question = models.CharField(max_length=255)
	body = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)


	def __unicode__(self):
		return self.body
 
	class Meta:
		ordering = ['created']		


