# https://www.twilio.com/login TWILIO ACCOUNT
# https://dashboard.ngrok.com/ NGROK
import sqlite3
import time
import cv2
import serial
from twilio.rest import Client
import sqlite3
import geocoder
distance = 0
difference = 0
ard = serial.Serial(PORT_NUMBER, 115200)
accountid = MESSAGE_TWILIO_ACCOUNT_ID 
auth = MESSAGE_TWILIO_AUTH_CODE
mess_client = Client(accountid, auth)
accountid = WHATSAPP_TWILIO_ACCOUNT_ID
auth = WHATSAPP_TWILIO_AUTH_CODE
fro = FROM_WHATSAPP_TWILIO_NUMBER
to = USER_WHATSAPP_NUMBER
whatsapp_client = Client(accountid, auth)
con = sq.connect(DATABASE_NAME)
excute = con.cursor()
n = 0
m = 0
vibration, smoke, flame = [0, 0, 0]
while True:
    for i in range(2):
        try:
            data = str(ard.readline(), encoding='utf-8')
        except:
            continue
        if 'distance' in data:
            distance = int(data[9:])
        elif 'difference' in data:
            difference = int(data[12:])
        elif 'smoke' in data:
            smoke = int(data[6:])
        elif 'flame' in data:
            flame = int(data[6:])
        elif 'vibration' in data:
            vibration = int(data[10:])
    print(difference)
    print(distance)
    if distance < 10 and difference > 5 and vibration == 1 and smoke == 1 and flame == 1:
        m += 1
        loc = geo.ip('me')
        location = loc.latlng
        link = f"https://maps.google.com/?q=loc:/{location[0]},{location[1]}"
        mess = mess_client.messages.create(from_="+19707172698", to=to[9 :],
                                           body=f"Accident detected\n GPS Location link: {link}")
        video = cv.VideoCapture(1)
        data = video.read()[1]
        cv.imwrite(FILE_LOCATION, data)
        im = cv.imread(FILELOCATION)
        video.release()
        mess = whatsapp_client.messages.create(body="evidences are found in the pictures and also in your database",
                                               media_url="NGROK_CONNECTION_ID/data/me.jpg",
                                               from_=fro, to=to)
        if m > 5:
            time.sleep(120)
    if distance < 10 or difference > 5:
        n += 1
        if n > 10:
            loc = geo.ip('me')
            location = loc.latlng
            link = f"https://maps.google.com/?q=loc:/{location[0]},{location[1]}"
            mess = mess_client.messages.create(from_="+19707172698", to=to[9:],
                                               body=f"Accident detected\n GPS Location link: {link}")
            n = 0
            time.sleep(120)
    elif distance < 10:
        print("object")
        video = cv.VideoCapture(1)
        data = video.read()[1]
        cv.imwrite("/xampp/htdocs/data/data.jpg", data)
        im = cv.imread('/xampp/htdocs/data/data.jpg')
        video.release()
        mess = whatsapp_client.messages.create(body="evidences are found in the pictures and also in your database",
                                               media_url="https://e3b8-2401-4900-4aa6-6402-9041-8733-34bb-e57a.in.ngrok.io/data/me.jpg",
                                               from_=fro, to=to)
        try:
            da = open('data.txt')
            x = int(da.read())
            da.close()
            excute.execute("INSERT INTO accident_evidence VALUES(?,?)", (f"{x+1}", sq.Binary(im[1])))
            con.commit()
            da = open('data.txt', 'w')
            da.write(str(x + 1))
            da.close()
            print('data stored')
        except sqlite3.DatabaseError:
            print("database not found")

    else:
        time.sleep(0.02)
