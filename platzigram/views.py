"""platzigram views"""
#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('oh, hi! Current server time is {now}'.format(now=str(now)))
