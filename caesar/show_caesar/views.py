# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader


def showcaesar(request):
    if request.is_ajax():
        getvalue = request.GET.get('value')
        print (getvalue)
    context = {}
    return render(request, 'show_caesar/show_caesar.html', context)
