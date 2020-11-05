""" Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_word(request):
    """ Return a geeting"""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now = str(now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs"))))

def numbers(request):
    """ Numbers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json')
    
