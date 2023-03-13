from Adafruit_IO import Client, Feed, Data, RequestError
import datetime
import time

import serial
import requests
import time
import numpy as np
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
def getAngle():
    file = open('/Users/ngimahyolmo/Desktop/me35/angles.txt','r')
    graph_data = file.read()
    lines = graph_data.split('\n')
    file.close()
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            x1 = float(x)
            y1 = float(y)
            xs =int(x1)
            ys =int(y1)
            return str(xs)+','+ str(ys)
        #aio.receive_next(temperature.key)
        


# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'KEY'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'aayushma'


aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
digital = aio.feeds('welcome-feed')

try:
    temperature = aio.feeds('midterm')
except RequestError:
    feed = Feed(name="LEGOooo")
    temperature = aio.create_feed(feed)

#
# Adding data
#
line= getAngle()

def adafruit():
    line= getAngle()
    try:
        aio.send_data(temperature.key, line)
    except:
        print("error")
    
    # works the same as send now
    #aio.append(temperature.key, line)

    # # setup batch data with custom created_at values
    # yesterday = (datetime.datetime.today() - datetime.timedelta(1)).isoformat()
    # today = datetime.datetime.now().isoformat()
    # data_list = [Data(value=50, created_at=today), Data(value=33, created_at=yesterday)]
    # # send batch data
    # aio.send_batch_data(temperature.key, data_list)

    #
    # Retrieving data
    #
# 
#     data = aio.receive_next(temperature.key)
#     print(data)
# 
#     data = aio.receive(temperature.key)
#     print(data)
# 
#     data = aio.receive_previous(temperature.key)
#     print(data)
    time.sleep(2)

theta_1 = [-2.69804832, -2.90983459, -3.02717846, -3.06183911, -3.01303047, -2.88536955,
-2.69498197, -2.46152119, -2.19346332, -1.8710115 ]
theta_2 = [1.15207409 ,1.51356078, 1.75649156 ,1.911902 ,  1.98548755 ,1.97683243,
1.88674649, 1.71625606, 1.45779614 ,1.07239498]

theta1= [np.rad2deg(t1) for t1 in theta_1]
theta2= [np.rad2deg(t2) for t2 in theta_2]
angles=[]
for x1, y1 in zip( theta1, theta2 ):
    angles.append( [ x1, y1 ] )


fred = mqtt.Client('aayu')

topic = "angles"

fred.connect('10.247.84.76')


def run():
    
    i=0
    while i < 10:




        def parser(message):
            t1 = ''
            t2 = ''
            comma = False 
            for letter in message:

                if (letter == ','):
                    comma = True
                elif (not comma and letter!='('):
                    t1 = t1 + letter
                elif(comma and  letter!=')'):
                    t2 = t2 + letter
            return float(t1), float(t2)

            started = False
                
        def trackMessage(user, userName, message):
            started=True
            x =  message.payload.decode()
            print("Message: " + x)
            t1, t2 = parser(x)

            file1 = open("/Users/ngimahyolmo/Desktop/me35/angles.txt", "w")
            text = str(t1)+','+str(t2)
            print(text)
            file1.write(text)
            file1.close()
            adafruit()

        # Subscription
        fred.on_message = trackMessage
        fred.loop_start()
        fred.subscribe(topic)

        t1 = str(angles[i][0]+90)
        t2 = str(angles[i][1])
        message = '(' + t1 +',' + t2 + ')'

        fred.publish(topic,message )
        # Run the loop for 2 seconds
        time.sleep(0.1)  
        #fred.loop_stop()
        i= i+1
        

while True:
    data = aio.receive(digital.key)
    if (data.value) == "ON":
        run()
    elif (data.value) == "OFF":
        print('received <- OFF\n')
    time.sleep(0.1)


fred.close()



