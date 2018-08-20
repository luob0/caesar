# -*- coding: utf-8 -*-
import csv
import pymysql


db = pymysql.connect("localhost","ruixin","123","caesarFinal")
cursor = db.cursor()

file=csv.reader(open('./S2_test.csv'))
i = 0
j = 1
for row in file:
    i = i+1
    # if i==1:
    if i>782036:
        id = j
        j = j+1
        # row[4] = "'"+row[4]+"'"
        if row[4] == '':
            row[4] = 'null'

        if row[5] == '':
            row[5] = 'null'
        else:
            row[5] = "'"+row[5]+"'"

        if row[6] == '':
            row[6] = 'null'

        if row[8] == '':
            row[8] = 'null'

        if row[14] == '':
            row[14] = 'null'
        else:
            row[14] = "'"+row[14]+"'"

        if row[16] == '':
            row[16] = 'null'

        if row[23] == '':
            row[23] = 'null'
        else:
            row[23] = "'"+row[23]+"'"

        if row[31] == '':
            row[31] = 'null'
        else:
            row[31] = "'"+row[31]+"'"

        if row[44] == '':
            row[44] = 'null'

        if row[54] == '':
            row[54] = 'null'
        mysql = "insert into show_caesar_caesardata value("+str(id)+","+row[1]+","+row[4]+","+row[5]+","+row[6]+","+row[8]+","+row[14]+","+row[16]+","+row[23]+","+row[31]+","+row[44]+","+row[54]+");"
        print(mysql)
        # print('\n')
        cursor.execute(mysql)
        db.commit()

        print('id: '+str(id))
        print('row1: '+row[1])
        print('row4: '+row[4])
        print('row5: '+row[5])
        print('row6: '+row[6])
        print('row8: '+row[8])
        print('row14: '+row[14])
        print('row16: '+row[16])
        print('row23: '+row[23])
        print('row31: '+row[31])
        print('row44: '+row[44])
        print('row54: '+row[54])
        print('\n')
        # if id == 217:
        #     exit(0)

db.close()
