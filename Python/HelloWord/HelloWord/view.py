# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'HHHHHHHHHHH Hello World!'
    return render(request, 'hello.html', context)

def engprotocal(request):
    return  render(request,'engprotocal.html')