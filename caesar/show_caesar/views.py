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
        module0 = trade.module0
        module1 = trade.module1
        module2 = trade.module2
        module3 = trade.module3
        module4 = trade.module4
        module5 = trade.module5
        module6 = trade.module6
        module7 = trade.module7
        module8 = trade.module8
        module9 = trade.module9
        module10 = trade.module10
        module11 = trade.module11
        module12 = trade.module12
        module13 = trade.module13
        module14 = trade.module14
        module15 = trade.module15
        module16 = trade.module16
        module17 = trade.module17
        module18 = trade.module18


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

        return HttpResponse(json.dumps({"module": module, "recall": recall, "disturb": disturb, "precision":precision, "accuracy": accuracy, "test": test,"p":p,"rr":r,"sa":s,"ae":a,"Transaction_ID":tradeid,"Transaction_Card_Number":cardnum,"Transaction_Card_Type":'dmxind01',"Transaction_Code":dmx10bytestring01,"Transaction_Type":dmx2bytestring02,"Transaction_Time":rqotrantimealt,"Transaction_Amount":tcaclientamt,"Merchant_Code":rua20bytestring001,"Signature_Verification_Method":ruaind004,"Customary_IP_Tag":dmxind03,"Fraudulent_Tag":sign,"module0":module0,"module1":module1,"module2":module2,"module3":module3,"module4":module4,"module5":module5,"module6":module6,"module7":module7,"module8":module8,"module9":module9,"module10":module10,"module11":module11,"module12":module12,"module13":module13,"module14":module14,"module15":module15,"module16":module16,"module17":module17,"module18":module18}))

    context = {}
    return render(request, 'show_caesar/show_caesar.html', context)
