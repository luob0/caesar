# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader


def showcaesar(request):
    context = {}
    return render(request, 'show_caesar/show_caesar.html', context)
