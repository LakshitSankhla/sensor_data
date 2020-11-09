import paho.mqtt.client as paho #mqtt library
import os
import json
import random
import time
from datetime import datetime

broker="mqtt.eclipse.org"
topic="sensor_data"
port=1883
ACCESS_TOKEN='zenatix'


def on_publish(client,userdata,result):
  print("published data is : ")
  pass

client= paho.Client("control1")
client.on_publish = on_publish
client.username_pw_set(ACCESS_TOKEN)
client.connect(broker,port,keepalive=60)

while True:
  temp = random.randint(22,28)
  humid=random.randrange(20,100)  ##random humidity between 20% and 80%
  machineStatus = True
  now = datetime.now()
  payload="{Temperature:"+str(temp)+"°C,"+"  "+"Humidity:"+str(humid)+"%"+"  "+"Machine Status:"+ str(machineStatus)+"  " +now.strftime("%Y-%m-%d %H:%M:%S")+"}"
  ret= client.publish(topic,payload)
  print(payload)
  print("Data Sent!!! \n")

  time.sleep(60)
