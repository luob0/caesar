# -*- conding:utf-8 -*-
import csv
import pymysql

db = pymysql.connect("localhost","ruixin","123","caesarFinal")
cursor = db.cursor()

file = csv.reader(open('./0809.csv'))
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
    if i > 1:
        if int(row[2]) == 1 and int(row[3]) == 1:
            tp = tp+1
        elif int(row[2]) == 0 and int(row[3]) == 0:
            tn = tn+1
        elif int(row[2]) == 1 and int(row[3]) ==0 :
            fp = fp+1
        elif int(row[2]) ==0 and int(row[3]) == 1:
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

        mysql = "insert into show_caesar_data value("+str(i-1)+","+str(accuracy)+","+str(precision)+","+str(recall)+","+str(disturb)+");"
        cursor.execute(mysql)
        # print (sql)
        db.commit()
        # print (i)
        # print ("tp:"+str(tp)+" tn:"+str(tn)+" fp:"+str(fp)+" fn:"+str(fn))
        # print ("recall:"+str(recall)+" disturb:"+str(disturb)+" precision:"+str(precision)+" accuracy:"+str(accuracy))
        # print ("")

db.close()
