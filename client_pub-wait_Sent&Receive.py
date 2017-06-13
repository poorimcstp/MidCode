#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2010-2013 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation
# Copyright (c) 2010,2011 Roger Light <roger@atchoo.org>
# All rights reserved.

# This shows a simple example of waiting for a message to be published.

import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
from Tkinter import *
def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if(msg.payload == "BREAK"):
        mqttc.unsubscribe("/Artorn/TP2")
    var.set(str(msg.payload))
    L1 = Label(top, textvariable = var)
    L1.update()

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    pass

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

def on_button():
    mqttc.publish("/Artorn/TP2", str(E1.get()), qos = 2)

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
def connect():
    mqttc.username_pw_set("PooridechM","DYeQFAXK28")
    mqttc.connect("km1.io", 1883, 60)
    mqttc.subscribe("/PooridechM/room1",qos = 2)
    var.set("Connected")
    L1 = Label(top, textvariable = var)
    L1.update()
    mqttc.loop_forever()
def on_unsubscribe(mqttc):
    print "Disconnected!"
    
# Uncomment to enable debug messages
# mqttc.on_log = on_log
top = Tk()
var = StringVar();
var.set("Hello")  
L1 = Label(top, textvariable = var)
L1.pack(side =LEFT)
B = Button(top, text = "Connect", command = connect)
E1 = Entry()
E1.pack(side = LEFT)
B.pack(side = LEFT)
D = Label(top, text = "Type BREAK in MQTT chat to sent message and connect agian",)
D.pack(side = RIGHT)
B2 = Button(top, text = "Sent", command = on_button)
B2.pack(side = LEFT)

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

top.mainloop()
