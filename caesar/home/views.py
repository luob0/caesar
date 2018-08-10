# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {}
    return render(request, 'home/home.html', context)

def signin(request):
    if request.is_ajax():
        getvalue = request.GET.get('value')
        print (getvalue)
    context = {}
    return render(request, 'home/signin.html', context)
