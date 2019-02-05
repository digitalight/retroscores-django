from django.db import models
from django.conf import settings
from django.utils import timezone

# The main score model

class Score(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    scoreResult = models.IntegerField()
    scoreGame = models.ForeignKey('Game', on_delete=models.CASCADE)
    scoreTimeDate = models.DateTimeField(default=timezone.now)
    scoreScreenShot = models.ImageField(upload_to='shots/%Y/%m/%d/')
    
    def publish(self):
        self.scoreTimeDate = timezone.now()
        self.save()


class Game(models.Model):
    gameName = models.CharField(max_length=200)
    gameYear = models.CharField(max_length=4)
    gameInfo = models.URLField()
    gameArtwork = models.ImageField(upload_to='artwork/')
    gameSystem = models.ForeignKey('System', on_delete=models.CASCADE)
    pass

    def __str__(self):
        return self.gameName


class System(models.Model):
    systemName = models.CharField(max_length=100)
    pass

    def __str__(self):
        return self.systemName