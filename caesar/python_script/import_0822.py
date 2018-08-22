# -*- coding: utf-8 -*-
import pymysql
import csv

# connect mysql
db = pymysql.connect("localhost","ruixin","123","caesarFinal")
cursor = db.cursor()

file=csv.reader(open('./0822.csv'))
i = 0
tp = 0
fn = 0
tn = 0
fp = 0
recall = 0.0
disturb = 0.0
precision = 0.0
accuracy = 0.0
for row in file:
    i = i+1
    if i>1:
        id = i-1
        tradeid = row[0]
        test=row[1]
        truth=row[2]
        module=row[3]
        p = row[4]
        r = row[5]
        s = row[6]
        a = row[7]

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

        mysql = "insert into show_caesar_trade value("+str(id)+","+tradeid+","+test+","+truth+","+module+","+p+","+r+","+s+","+a+","+str(round(accuracy,2))+","+str(round(disturb,2))+","+str(round(precision,2))+","+str(round(recall,2))+");"
        # print (mysql)
        # cursor.execute("insert into show_caesar_transaction value("+id+","+tradeid+","+module+","+test+","+truth+");")
        cursor.execute(mysql)
        db.commit()
        print (i)

db.close()
