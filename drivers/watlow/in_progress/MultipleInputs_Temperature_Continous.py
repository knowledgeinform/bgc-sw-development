# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:16:36 2023

@author: moonnt1
"""
# This code read the output of Analog Input 1 and Analog Input 2 from the
# Watlow EZ-Zone and plots both outputs continuously verses time

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
y1 = []
y2 = []


while True:
    plt.clf()
    CurrentTime = datetime.datetime.now()

    # Analog Input Value: View the process value. Registry value of 380
    # (low bytes) or 381 (high bytes), off set 90 for each analog input after 1
    LowBits1 = cast(int, instrument.read_register(380))
    HighBits1 = cast(int, instrument.read_register(381))
    LowBits2 = cast(int, instrument.read_register(470))
    HighBits2 = cast(int, instrument.read_register(471))

    RawTemp1 = (HighBits1 << 16) + LowBits1
    s1 = pack(">L", RawTemp1)
    Fahrenheit1 = unpack(">f", s1)[0]

    RawTemp2 = (HighBits2 << 16) + LowBits2
    s2 = pack(">L", RawTemp2)
    Fahrenheit2 = unpack(">f", s2)[0]

    # Celsius1 = (Fahrenheit1 - 32) * 5.0/9.0
    # Celsius2 = (Fahrenheit2 - 32) * 5.0/9.0

    print(str(CurrentTime) + " -- " + "Analog 1: " + str(float(Fahrenheit1)) + " Analog 2: " + str(float(Fahrenheit2)))

    # plotting Temp vs Time
    y1.append(Fahrenheit1)
    y2.append(Fahrenheit2)
    x.append(CurrentTime)

    plt.clf()
    plt.scatter(x, y1, label="Input 1")
    plt.scatter(x, y2, label="Input 2")
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.xlabel("Time")
    plt.ylabel("Analog Input Temperature")
    plt.legend(loc="upper left")
    plt.pause(1)

    time.sleep(1)
