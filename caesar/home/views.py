# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.http import HttpResponse
import json


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {}
    return render(request, 'home/home.html', context)

def signin(request):
    if request.is_ajax():
        getvalue = request.GET.get('value')
        passwd = "wangcheng214"
        if getvalue==passwd:
            return HttpResponse(json.dumps({"result":1}))
        else:
            return HttpResponse(json.dumps({"result":0}))
        # print (getvalue)
    context = {}
    return render(request, 'home/signin.html', context)
