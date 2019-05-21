#!/usr/bin/python
# Author: Joe McCormack

import socket
import time
import requests
import Adafruit_MCP9808.MCP9808 as MCP9808

url = '<URL>' #NEED TO FIX THIS WITH A VARIABLE LATER

#Define function for Celcius to Fahrenheit
def c_to_f(c):
        return c * 9.0 / 5.0 + 32.0

#Read in hostname to variable
hostname = socket.gethostname()

#Sensor using default I2C address (0x18) and default I2C bus
#See documentation for MCP9808 if other I2C settings are needed
sensor = MCP9808.MCP9808()

#Initialize communication with sensor
sensor.begin()

#Read in Celcius temp
pytemp = sensor.readTempC()

#Write device name and Fahrenheit temp to payload
payload = {'pyname': hostname, 'temp': c_to_f(pytemp)}

#POST payload to URL
r = requests.post(url, data=payload)
r.text
r.status_code
