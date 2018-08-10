# -*- coding: utf-8 -*-
import pymysql
import csv

# connect mysql
db = pymysql.connect("localhost","ruixin","123","caesarFinal")
cursor = db.cursor()

file=csv.reader(open('../0809.csv'))
i=0
for row in file:
    i = i+1
    if i>1:
        id = i-1
        tradeid = row[0]
        module = row[1]
        test = row[2]
        truth = row[3]
        mysql = "insert into show_caesar_transaction value("+str(id)+","+tradeid+","+module+","+test+","+truth+");"
        # print (mysql)
        # cursor.execute("insert into show_caesar_transaction value("+id+","+tradeid+","+module+","+test+","+truth+");")
        cursor.execute(mysql)
        db.commit()
        print (i)

db.close()
