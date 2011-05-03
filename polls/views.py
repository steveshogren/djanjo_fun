from django.template import Context, loader
from django.http import HttpResponse
from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
#    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(t.render(c))

def detail(request, poll_id):
    return HttpResponse("You are looking at poll %s" % poll_id)

def results(request, poll_id):
    return HttpResponse("You are loking at results of poll %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("You are voting for poll %s" % poll_id)
