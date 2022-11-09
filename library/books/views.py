from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint

# Create your views here.
def get_books(request):
    if request.method == 'GET':
        print('it was a get request')
    else:
        print('not a get request')
        
    return HttpResponse("Hello, world. You're at the books index.")