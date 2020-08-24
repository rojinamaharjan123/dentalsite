from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime 

# Create your models here.

class  TimeStamp(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		abstract =True



class Category(TimeStamp):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	image = models.ImageField(upload_to="category")

	def __str__(self):
		return self.title
		


class Customer(TimeStamp):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name =  models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	age = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

	def save(self, *args,**kwargs):
		grp , created = Group.object.get_or_create(name="customer")

		self.groups.add(grp)
		super.save(*args,**kwargs)

	def __str__(self):
		return self.name
		


class Services(TimeStamp):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	fav_icon = models.CharField(max_length=100, null =True , blank =True)

	def __str__(self):
		return self.title
		
class Admin(TimeStamp):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	age = models.CharField(max_length=100)

	def save(self, *args,**kwargs):
		grp , created = Group.object.get_or_create(name="Admin")

		self.groups.add(grp)
		super.save(*args,**kwargs)

	def __str__(self):
		return self.name
		

class Website(TimeStamp):
	name = models.CharField(max_length=100)
	logo = models.ImageField(upload_to="logo")
	email = models.EmailField()
	phone_no = models.CharField(max_length=50)
	address = models.CharField(max_length=100, null=True, blank=True)
	facebook = models.CharField(max_length=100, null=True, blank=True)
	twitter = models.CharField(max_length=100, null=True, blank=True)
	instagram = models.CharField(max_length=100, null=True, blank=True)
	about = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name



class Carousel(TimeStamp):
	title=models.CharField(max_length=100)
	slogan=models.CharField(max_length=100)
	image=models.ImageField(upload_to="Carousel")
	link= models.CharField(max_length=100 , null=True , blank = True)
	def __str__(self):
		return self.title



class Subscription(TimeStamp):
	email = models.EmailField()
	



class WorkingHour(TimeStamp):
	day = models.CharField(max_length = 100)
	starttime = models.TimeField()
	endtime = models.TimeField()



class Freeconsultation(TimeStamp):
	Fullname = models.CharField(max_length=100)
	phone_no =  models.CharField(max_length=100)
	email = models.EmailField()
	# DentalCrowns = models.
	message = models.CharField(max_length=100)


