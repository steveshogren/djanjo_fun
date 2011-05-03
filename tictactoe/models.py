from django.db import models
#import datetime


class Game(models.Model):
    name = models.CharField(max_length=200)

class Player(models.Model):
#    def __unicode__(self):
#        return self.choice
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=200)

class Move(models.Model):
    character = models.CharField(max_length=2)

class GameBoard(models.Model):
#    def __unicode__(self):
#        return self.question
#
#    def was_published_today(self):
#        return self.pub_date.date() == datetime.date.today()

    x = models.IntegerField()
    y = models.IntegerField()
    move = models.ForeignKey(Move)
    game = models.ForeignKey(Game)
