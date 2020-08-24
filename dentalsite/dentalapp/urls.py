from django.urls import *
from .views import *
app_name="dentalapp"

urlpatterns = [
	path("home/" ,HomeView.as_view(), name="clienthome"),
]