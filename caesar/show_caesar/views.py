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
        tradeid = Transaction.objects.get(id=getvalue).tradeid
        module = Transaction.objects.get(id=getvalue).module
        test = Transaction.objects.get(id=getvalue).test
        recall = round(Data.objects.get(id=getvalue).recall, 2)
        disturb = round(Data.objects.get(id=getvalue).disturb, 2)
        precision = round(Data.objects.get(id=getvalue).precision, 2)
        accuracy = round(Data.objects.get(id=getvalue).accuracy, 2)
        # print (accuracy)

        # database table: show_caesar_moduler
        rtest_tmp = ModuleR.objects.get(rid=tradeid).test
        # database table: show_caesar_modules
        stest_tmp = ModuleS.objects.get(sid=tradeid).test
        # database table: show_caesar_modulea
        atest_tmp = ModuleA.objects.get(aid=tradeid).test
        # database table: show_caesar_modulep
        ptest_tmp = ModuleP.objects.get(pid=tradeid).test
        if rtest_tmp:
          rtest = 1
        else:
          rtest = 0
        if stest_tmp:
          stest = 1
        else:
          stest = 0
        if atest_tmp:
          atest = 1
        else:
          atest = 0
        if ptest_tmp:
          ptest = 1
        else:
          ptest = 0

        # database table: show_caesar_caesardata
        cardnum = CaesarData.objects.get(caesarid=tradeid).cardnum
        dmxind01 = CaesarData.objects.get(caesarid=tradeid).dmxind01
        dmx10bytestring01 = CaesarData.objects.get(caesarid=tradeid).dmx10bytestring01
        dmx2bytestring02 = CaesarData.objects.get(caesarid=tradeid).dmx2bytestring02
        rqotrantimealt = CaesarData.objects.get(caesarid=tradeid).rqotrantimealt
        tcaclientamt = CaesarData.objects.get(caesarid=tradeid).tcaclientamt
        rua20bytestring001 = CaesarData.objects.get(caesarid=tradeid).rua20bytestring001
        ruaind004 = CaesarData.objects.get(caesarid=tradeid).ruaind004
        dmxind03 = CaesarData.objects.get(caesarid=tradeid).dmxind03
        sign = CaesarData.objects.get(caesarid=tradeid).sign

        return HttpResponse(json.dumps({"module": module, "recall": recall, "disturb": disturb, "precision":precision, "accuracy": accuracy, "test": test,"p":ptest,"rr":rtest,"sa":stest,"ae":atest,"Transaction_ID":tradeid,"Transaction_Card_Number":cardnum,"Transaction_Card_Type":'dmxind01',"Transaction_Code":dmx10bytestring01,"Transaction_Type":dmx2bytestring02,"Transaction_Time":rqotrantimealt,"Transaction_Amount":tcaclientamt,"Merchant_Code":rua20bytestring001,"Signature_Verification_Method":ruaind004,"Customary_IP_Tag":dmxind03,"Fraudulent_Tag":sign}))

    context = {}
    return render(request, 'show_caesar/show_caesar.html', context)
