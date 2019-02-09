from django.urls import path
from . import views

urlpatterns = [
	path('', views.scores_list, name='scores_list'),
	path('game/<int:pk>/', views.game_single, name='game_single'),
	path('games', views.games, name='games'),
]
