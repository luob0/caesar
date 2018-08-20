# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader
from show_caesar.models import Transaction, Data, ModuleS, ModuleA, ModuleR, ModuleP, CaesarData
from django.http import HttpResponse
import json


def showcaesar(request):
    if request.is_ajax():
        getvalue = int(request.GET.get('value'))
        print (getvalue)

        # database table: show_caesar_transaction
        tradeid = Transaction.objects.get(id=getvalue).tradeid
        module = Transaction.objects.get(id=getvalue).module
        test = Transaction.objects.get(id=getvalue).test
        recall = round(Data.objects.get(id=getvalue).recall, 2)
        disturb = round(Data.objects.get(id=getvalue).disturb, 2)
        precision = round(Data.objects.get(id=getvalue).precision, 2)
        accuracy = round(Data.objects.get(id=getvalue).accuracy, 2)

        return HttpResponse(json.dumps({"module": module, "recall": recall, "disturb": disturb, "precision":precision, "accuracy": accuracy, "test": test,"rtest":1,"stest":0,"atest":0,"cardnum":1111111,"dmxind01":'c',"dmx10bytestring01":12107,"dmx2bytestring02":13,"rqotrantimealt":2017/6/1,"tcaclientamt":728.92,"rua20bytestring001":123,"ruaind004":1,"dmxind03":0,"sign":0}))

    context = {}
    return render(request, 'show_caesar/show_caesar.html', context)
