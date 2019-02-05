"""platzigram views"""
#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('oh, hi! Current server time is {now}'.format(now=str(now)))


def sort_integers(request):
    """Return a json response!"""
    numbers = sorted(
        [int(i) for i in request.GET['numbers'].split(',')]
    )
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted',
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type="application/json"
    )


def say_hi(request,name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to platzigram'.format(name)
    return HttpResponse(message)
