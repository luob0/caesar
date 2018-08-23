# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import loader
from show_caesar.models import Trade, CaesarData
from django.http import HttpResponse
import json


def showcaesar(request):
    if request.is_ajax():
        getvalue = int(request.GET.get('value'))
        print (getvalue)

        # Get data from show_caesar_trade table
        trade = Trade.objects.get(id=getvalue)
        tradeid = trade.tradeid
        test = trade.test
        module = trade.module
        recall = trade.recall
        accuracy = trade.accuracy
        disturb = trade.disturb
        precision = trade.precision
        p = trade.p
        r = trade.r
        s = trade.s
        a = trade.a

        # Get data from show_caesar_caesardata table
        caesardata = CaesarData.objects.get(caesarid=tradeid)
        cardnum = caesardata.cardnum
        dmxind01 = caesardata.dmxind01
        dmx10bytestring01 = caesardata.dmx10bytestring01
        dmx2bytestring02 = caesardata.dmx2bytestring02
        rqotrantimealt = caesardata.rqotrantimealt
        tcaclientamt = caesardata.tcaclientamt
        rua20bytestring001 = caesardata.rua20bytestring001
        ruaind004 = caesardata.ruaind004
        dmxind03 = caesardata.dmxind03
        sign = caesardata.sign

        return HttpResponse(json.dumps({"module": module, "recall": recall, "disturb": disturb, "precision":precision, "accuracy": accuracy, "test": test,"p":p,"rr":r,"sa":s,"ae":a,"Transaction_ID":tradeid,"Transaction_Card_Number":cardnum,"Transaction_Card_Type":'dmxind01',"Transaction_Code":dmx10bytestring01,"Transaction_Type":dmx2bytestring02,"Transaction_Time":rqotrantimealt,"Transaction_Amount":tcaclientamt,"Merchant_Code":rua20bytestring001,"Signature_Verification_Method":ruaind004,"Customary_IP_Tag":dmxind03,"Fraudulent_Tag":sign}))

        # return HttpResponse(json.dumps({"tradeid":tradeid,"test":test,"module":module,"recall":recall,"accuracy":accuracy,"disturb":disturb,"precision":precision,"p":p,"r":r,"s":s,"a":a}))
        # tradeid = Trade.objects.get(id=getvalue).tradeid
        # test = Trade.objects.get(id=getvalue).test
        # module = Trade.objects.get(id=getvalue).module
    context = {}
    return render(request, 'show_caesar/show_caesar.html', context)
