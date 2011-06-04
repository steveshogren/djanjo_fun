from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from tictactoe.models import Game

def index(request):
#    game_list = Game.objects.all()[:5]
    return HttpResponse("the game page, has ")

def game(request, game_id):
    return HttpResponse("Game id " + game_id)
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})