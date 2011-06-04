from django.conf.urls.defaults import *
#from polls.models import Poll

urlpatterns = patterns('',
    (r'^$', 'tictactoe.views.index'),
#    (r'^/(?P<game_id>\d+)/$', 'tictactoe.views.game'),
    (r'^game/(?P<game_id>\d+)/$', 'tictactoe.views.game'),
)
