from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.

class HomeView (TemplateView):
	template_name = "clienttemplates/clienthome.html"


	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['allcarousel'] = Carousel.objects.all()
		context['org'] = Website.objects.all().first()
		context['services'] = Services.objects.all()

		return context
