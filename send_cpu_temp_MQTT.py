import paho.mqtt.client as mqtt
import time
from subprocess import check_output
import json
import os

def try_connecting():
    global is_connected
    try:
        ourClient.connect("mqtt.beia-telemetrie.ro", 1883)
        is_connected=True
        tmp_arr=[]
        try:
            with open("/home/pi/Desktop/Sterea_Andrei_Mihai/temporary.log", "r") as tmp:
                for x in tmp:
                    tmp_arr.append(str(x))
                os.remove("home/pi/Desktop/Sterea_Andrei_Mihai/temporary.log")
        except:
            pass
        for x in tmp_arr:
            ourClient.publish("training/device/Sterea_Andrei_Mihai", str(x))
            timesleep(0.1)
    except:
        print("No MQTT connection at the moment..")
        is_connected=False
is_connected=False
ourClient=mqtt.Client("practical task")

while True:
    try_connecting()
    try:
        temp= str(check_output("/opt/vc/bin/vcgencmd measure_temp", shell=True))
        info={"temp_CPU":temp[7:11]}
        print(info)
        with open("/home/pi/Desktop/Sterea_Andrei_Mihai/Sterea_Andrei_Mihai.log","a") as log:
            log.write(str(info)+"\n")
        if is_connected:
            ourClient.publish("training/device/Sterea_Andrei_Mihai", json.dumps(info))
        else:
            with open("/home/pi/Desktop/Sterea_Andrei_Mihai/temporary.log", "a") as tmp:
                tmp.write(json.dumps(info)+ "\n")
        time.sleep(5)
    except Exception as e:
        print("Exception: " + str(e)) 
