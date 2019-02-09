from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Score, Game, System

# Create your views here.

def scores_list(request):
	#Get latest 5 scores
	scores = Score.objects.filter(scoreTimeDate__lte=timezone.now()).order_by('-scoreTimeDate')[:12]
	return render(request, 'scores/scores_list.html', {'scores':scores})

def game_single(request, pk):
	game = get_object_or_404(Game, pk=pk)
	scores = Score.objects.filter(scoreGame__pk=pk).order_by('-scoreResult')
	return render(request, 'scores/game_single.html', {'game': game, 'scores': scores})

def games(request):
	games = Game.objects.all().order_by('gameName')
	return render(request, 'scores/games.html', {'games':games})
