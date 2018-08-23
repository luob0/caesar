# -*- coding: utf-8 -*-
from __future__ import division
import pymysql
import csv

# connect mysql
db = pymysql.connect("localhost","ruixin","123","caesarFinal")
cursor = db.cursor()

file=csv.reader(open('/home/ruixin/Projects_Databak/0822.csv'))
i = 0
tp = 0
fn = 0
tn = 0
fp = 0
recall = 0.0
disturb = 0.0
precision = 0.0
accuracy = 0.0
select = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
per_select = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
for row in file:
    i = i+1
    if i>1:
        per_select = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        print(i)
        id = i-1
        tradeid = row[0]
        test=row[1]
        truth=row[2]
        module=row[3]
        p = row[4]
        r = row[5]
        s = row[6]
        a = row[7]
        select[int(module)] = select[int(module)] + 1
        # print(2/sum(select))
        for j in range(0,19):
            per_select[j] = round(select[j]/sum(select)*100,2)

        print(select)
        print(per_select)
        print(sum(select))
        # print(sum_select)
        print("\n")

        if int(row[1]) == 1 and int(row[2]) == 1:
            tp = tp+1
        elif int(row[1]) == 0 and int(row[2]) == 0:
            tn = tn+1
        elif int(row[1]) == 1 and int(row[2]) ==0 :
            fp = fp+1
        elif int(row[1]) ==0 and int(row[2]) == 1:
            fn = fn+1
        else:
            print ("error!")

        if (tp+fn)==0:
            recall = 100.0
        else:
            recall = (tp*100.0)/(tp+fn)

        if (tn+fp)==0:
            disturb = 0.0
        else:
            disturb = (fp*100.0)/(tn+fp)

        if (tp+fp)==0:
            precision = 0.0
        else:
            precision = (tp*100.0)/(tp+fp)

        if (tp+tn+fp+fn)!=0:
            accuracy = ((tp+tn)*100.0)/(tp+tn+fp+fn)

        mysql = "insert into show_caesar_trade value("+str(id)+","+tradeid+","+test+","+truth+","+module+","+p+","+r+","+s+","+a+","+str(round(accuracy,2))+","+str(round(disturb,2))+","+str(round(precision,2))+","+str(round(recall,2))+","+str(per_select[0])+","+str(per_select[1])+","+str(per_select[10])+","+str(per_select[11])+","+str(per_select[12])+","+str(per_select[13])+","+str(per_select[14])+","+str(per_select[15])+","+str(per_select[16])+","+str(per_select[17])+","+str(per_select[18])+","+str(per_select[2])+","+str(per_select[3])+","+str(per_select[4])+","+str(per_select[5])+","+str(per_select[6])+","+str(per_select[7])+","+str(per_select[8])+","+str(per_select[9])+");"
        # print (mysql)
        # cursor.execute("insert into show_caesar_transaction value("+id+","+tradeid+","+module+","+test+","+truth+");")
        cursor.execute(mysql)
        db.commit()
        # print (i)

db.close()
