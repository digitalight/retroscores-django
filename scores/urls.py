from django.urls import path
from . import views

urlpatterns = [
	path('', views.scores_list, name='scores_list'),
]