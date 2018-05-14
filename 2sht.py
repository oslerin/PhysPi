#!user/bin/env python

#INITIAL AUTHOR: Erin Osler (2018, CU-ITk)
#this code activates the serial connection between the arduino and the raspberry pi and dumps recorded data into the MySQL database
#initially, the arduino is connected in serial with the correct port and baudrate
#data for date, time, and temperature and humidity values from each of two the two SHT's is read in
#once data has been read from the second SHT (meaning that all data has been obtained for one run) the values are input into the database called 2SHT

import serial
import MySQLdb as mdb
import datetime

#function to determine whether or not a given value is a float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

db = mdb.connect("localhost", "cuitkuser", "cuitk", "2sht")

arduino = serial.Serial("/dev/ttyACM0")
arduino.baudrate = 9600
gotone=False
gottwo=False
while(1):
    data = arduino.readline()
    datasplit = data.split(":")
    if datasplit[0] == '1':
        if not is_float(datasplit[1]):
            continue
        temp1 = datasplit[1]
        if not is_float(datasplit[2]):
            continue
        hum1 = datasplit[2]
        gotone=True
        print temp1
        print hum1
    elif datasplit[0] == '2':
        if not gotone:
            continue
        if not is_float(datasplit[1]):
            continue
        temp2 = datasplit[1]
        if not is_float(datasplit[2]):
            continue
        hum2 = datasplit[2]
        gottwo=True
        print temp2
        print hum2
    else:
        continue
    if gottwo:
        with db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO temphum(Date, Time, temp1, hum1, temp2, hum2) VALUES(%s, %s, %s, %s, %s, %s)",(datetime.datetime.now().date(), datetime.datetime.now().time(), temp1, hum1, temp2, hum2))
            db.commit()
            cursor.close()       
        gottone=False
        gottwo=False
