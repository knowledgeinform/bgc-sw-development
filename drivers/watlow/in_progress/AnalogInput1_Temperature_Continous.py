# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 08:47:45 2023

@author: moonnt1
"""

# This code reads the Analog Input 1 Value for the Watlow EZ-Zone and
# plots the continous output as a funciton of Time

from struct import pack, unpack
from typing import cast
import minimalmodbus
import time
import datetime
import matplotlib.pyplot as plt


class WatLow:
    def __init__(self, addr, baudrate):
        self.address = addr
        self.baudrate = baudrate


# Communicating to Watlow EZ-Zone
controller = WatLow(1, 9600)
# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument("COM7", controller.address)
assert instrument.serial is not None
instrument.serial.baudrate = controller.baudrate


x = []
y = []


while True:
    CurrentTime = datetime.datetime.now()

    # Analog Input Value: View the process value. Registry value of 380
    # (low bytes) or 381 (high bytes), off set 90 for each analog input after 1
    LowBits = cast(int, instrument.read_register(380))
    HighBits = cast(int, instrument.read_register(381))
    RawTemp = (HighBits << 16) + LowBits
    s = pack(">L", RawTemp)
    Fahrenheit = unpack(">f", s)[0]
    Celsius = (Fahrenheit - 32) * 5.0 / 9.0

    print(str(CurrentTime) + " -- " + str(float(Celsius)))

    # plotting Temp vs Time
    y.append(Celsius)
    x.append(CurrentTime)

    plt.clf()
    plt.scatter(x, y)
    plt.xlabel("Time")
    plt.ylabel("Analog Input 1 Temperature")
    plt.plot(x, y)
    plt.pause(0.5)
    plt.clf()
    plt.draw()

    time.sleep(1)
