# -*- coding: utf-8 -*-
import pymysql
import csv


# connect mysql
db = pymysql.connect("localhost","ruixin","123","caesarFinal")
cursor = db.cursor()

file=csv.reader(open('./module_P.csv'))
i=0
j = 1
for row in file:
    i = i+1
    if i>782036:
        id = j
        j = j+1
        pid = row[0]
        test = row[1]
        truth = row[2]
        mysql = "insert into show_caesar_modulep value("+str(id)+","+pid+","+test+","+truth+");"
        # print (mysql)
        # cursor.execute("insert into show_caesar_transaction value("+id+","+tradeid+","+module+","+test+","+truth+");")
        cursor.execute(mysql)
        db.commit()
        print (i)

db.close()
