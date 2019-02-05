from django.shortcuts import render
from django.utils import timezone
from .models import Score, Game, System

# Create your views here.

def scores_list(request):
	scores = Score.objects.filter(scoreTimeDate__lte=timezone.now()).order_by('scoreTimeDate')
	return render(request, 'scores/scores_list.html', {'scores':scores})