""" Platzigram views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime


def hello_word(request):
    """ Return a geeting"""
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now = str(now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs"))))

def numbers(request):
    """ Numbers."""
    numbers = request.GET['numbers']
    return HttpResponse(f'Hi! Franco. Numeros de la URL: {str(numbers)}')
