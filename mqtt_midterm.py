import serial
import requests
import time
import numpy as np
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style



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

fred.connect('10.245.155.186')

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
    file1.write(text)
    file1.close()
    



    


# Subscription
fred.on_message = trackMessage
fred.loop_start()
fred.subscribe(topic)

while True:
    for angle in angles:
        t1 = str(angle[0]+90)
        t2 = str(angle[1])
        message = '(' + t1 +',' + t2 + ')'
        
        fred.publish(topic,message )
        # Run the loop for 2 seconds
        time.sleep(1)  
        #fred.loop_stop()



