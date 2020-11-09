import paho.mqtt.client as paho
import smtplib, ssl
import datetime
import json
import time

broker = "localhost"
topic = "sensor_data"
temp=[]
humid=[]
humid_avg=[]
port = 465                             # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "myemail@gmail.com"          # Enter your address
receiver_email = "youremail@gmail.com"      # Enter receiver address
password = "Type your password here"

start="sensor_data"
with open('data_sensors.json', 'w') as file:
    json.dump(start, file)

def on_message(client, userdata, message):
    print("received data is :")
    print(str(message.payload.decode("utf-8")))
    print("")
    temp.append(int(message.payload.decode("utf-8")[13:15]))
    humid.append(int(message.payload.decode("utf-8")[29:31]))

    if int(len(humid)>4):
        humid_avg.append(sum(humid[-5:])/5)
        if(int(len(humid_avg)>4)):
            if(humid_avg[0]>80 and humid_avg[1]>80 and humid_avg[2]>80 and humid_avg[3]>80 and humid_avg[4]>80 ):
                '''message = "Warning!!!!Humidity greater than 80%!!!"
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)'''
                print("Warning Email Sent!!")
            humid_avg.pop(0)
        humid.pop(0)
    if(int(message.payload.decode("utf-8")[13:15]))>28:
        print("High Temprature")
    if (int(message.payload.decode("utf-8")[13:15]))<22:
        print("Low Temprature")
    if(message.payload.decode("utf-8")[49:54] == "False"):
        print("Machine Off")

    data=str({message.payload.decode("utf-8")})

    with open('data_sensors.json', 'r') as j:
        json_data = json.load(j)
    data =json_data + data
    with open('data_sensors.json', 'w') as file:
        json.dump(data, file)


client = paho.Client("user")
client.on_message = on_message

print("connecting to broker host", broker)
client.connect(broker)
print("subscribing begins here")
client.subscribe(topic)

while 1:
    client.loop_forever()