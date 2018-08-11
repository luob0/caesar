# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader
from show_caesar.models import Transaction, Data
from django.http import HttpResponse
import json


def showcaesar(request):
    if request.is_ajax():
        getvalue = int(request.GET.get('value'))
        print (getvalue)
        module = Transaction.objects.get(id=getvalue).module
        test = Transaction.objects.get(id=getvalue).test
        recall = round(Data.objects.get(id=getvalue).recall, 2)
        disturb = round(Data.objects.get(id=getvalue).disturb, 2)
        precision = round(Data.objects.get(id=getvalue).precision, 2)
        accuracy = round(Data.objects.get(id=getvalue).accuracy, 2)
        # print (accuracy)
        return HttpResponse(json.dumps({"module": module, "recall": recall, "disturb": disturb, "precision":precision, "accuracy": accuracy, "test": test}))

    context = {}
    return render(request, 'show_caesar/show_caesar.html', context)
