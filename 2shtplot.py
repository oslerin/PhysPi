#!user/bin/env python

#INITIAL AUTHORS: Erin Osler and James Botte (2018, CU-ITk)
#this will extract the last hours data into a file called log.dat which will then be used to plot the temperature and humidity over time

import MySQLdb as mdb
import datetime
from datetime import timedelta

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def dump_cursor(cursor):
    try:
        results=cursor.fetchall()
        for row in results:
            print("%s,%s,%s,%s,%s,%s" % (row[0], row[1], row[2]. row[3], row[4], row[5]))
    except:
        print("error: couldn't fetch data")
                

db = mdb.connect("localhost", "cuitkuser", "cuitk", "2sht")
f = open('log.dat', 'w')
with db:
    cursor = db.cursor()
    try:
        cursor.execute("select Date, Time, temp1, hum1, temp2, hum2 from temphum where Date=%s and Time>%s", ((datetime.datetime.now()-timedelta(hours=1)).date(), (datetime.datetime.now()-timedelta(hours=1)).time()))
        results=cursor.fetchall()
        for row in results:
            if row[2] < 100 and row[3] < 100 and row[4] < 100 and row[5] < 100:
                print >>f,("%s %s,%0.2f,%0.2f,%0.2f,%0.2f"%(row[0], row[1], row[2], row[3], row[4], row[5]))
    except Exception as e:
        print("error: couldn't fetch data")
        print str(e)
    cursor.close()
    f.close()   
