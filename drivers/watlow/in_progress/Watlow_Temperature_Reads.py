# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:23:17 2023

Script to only read and graph temperature 

@author: moonnt1
"""

# importing required functions
import minimalmodbus
import time
import datetime
import matplotlib.pyplot as plt
from struct import pack, unpack
from typing import cast


# establishing communication with Watlow
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

# plotting temepratures for data monitoring
x = []
y1 = []
# y2=[]
# y3=[]
# y4=[]
# y5=[]
# y6=[]

while True:
    CurrentTime = datetime.datetime.now()
    # Analog Input Value: View the process value. Registry value of 380
    # (low bytes) or 381 (high bytes), off set 90 for each analog input after 1
    V1_LowBits = cast(int, instrument.read_register(380))
    V1_HighBits = cast(int, instrument.read_register(381))
    V1_RawTemp = (V1_HighBits << 16) + V1_LowBits
    V1_s = pack(">L", V1_RawTemp)
    V1_Fahrenheit = unpack(">f", V1_s)[0]
    V1_Celsius = (V1_Fahrenheit - 32) * 5.0 / 9.0

    # V2A_LowBits = cast(int, instrument.read_register(470))
    # V2A_HighBits = cast(int, instrument.read_register(471))
    # V2A_RawTemp = (V2A_HighBits << 16) + V2A_LowBits
    # V2A_s = pack('>L', V2A_RawTemp)
    # V2A_Fahrenheit = unpack('>f',V2A_s)[0]
    # V2A_Celsius = (V2A_Fahrenheit - 32) * 5.0/9.0

    # V2B_LowBits = cast(int, instrument.read_register(560))
    # V2B_HighBits = cast(int, instrument.read_register(561))
    # V2B_RawTemp = (V2B_HighBits << 16) + V2B_LowBits
    # V2B_s = pack('>L', V2B_RawTemp)
    # V2B_Fahrenheit = unpack('>f',V2B_s)[0]
    # V2B_Celsius = (V2B_Fahrenheit - 32) * 5.0/9.0

    # V3_LowBits = cast(int, instrument.read_register(560))
    # V3_HighBits = cast(int, instrument.read_register(561))
    # V3_RawTemp = (V3_HighBits << 16) + V3_LowBits
    # V3_s = pack('>L', V3_RawTemp)
    # V3_Fahrenheit = unpack('>f',V3_s)[0]
    # V3_Celsius = (V3_Fahrenheit - 32) * 5.0/9.0

    # FPD_LowBits = cast(int, instrument.read_register(1010))
    # FPD_HighBits = cast(int, instrument.read_register(1011))
    # FPD_RawTemp = (FPD_HighBits << 16) + FPD_LowBits
    # FPD_s = pack('>L', FPD_RawTemp)
    # FPD_Fahrenheit = unpack('>f',FPD_s)[0]
    # FPD_Celsius = (FPD_Fahrenheit - 32) * 5.0/9.0

    # XFer_In_LowBits = cast(int, instrument.read_register(830))
    # XFer_In_HighBits = cast(int, instrument.read_register(831))
    # XFer_In_RawTemp = (XFer_In_HighBits << 16) + XFer_In_LowBits
    # XFer_In_s = pack('>L', XFer_In_RawTemp)
    # XFer_In_Fahrenheit = unpack('>f',XFer_In_s)[0]
    # Xfer_In_Celsius = (XFer_In_Fahrenheit - 32) * 5.0/9.0

    # plotting Temp vs Time
    y1.append(V1_Celsius)
    x.append(CurrentTime)
    # y2.append(V2A_Celsius)
    # y3.append(V2B_Celsius)
    # y4.append(V3_Celsius)
    # y5.append(FPD_Celsius)
    # y6.append(XFer_In_Celsius)

    plt.clf()
    plt.scatter(x, y1, label="Valve Oven Zone 1")
    # plt.scatter(x,y2, label='Valve Oven Zone 2A')
    # plt.scatter(x,y3, label= 'Valve Oven Zone 2B')
    # plt.scatter(x,y4, label= 'Valve Oven Zone 3')
    # plt.scatter(x,y5, label= 'FPD Block')
    # plt.scatter(X,y6, label= 'Columne Transer In')
    plt.plot(x, y1)
    # plt.plot(x,y2)
    # plt.plot(x,y3)
    # plt.plot(x,y4)
    # plt.plot(x,y5)
    # plt.plot(x,y6)
    plt.xlabel("Time")
    plt.ylabel("Analog Input Temperature")
    plt.legend(loc="upper left")
    plt.pause(1)
    plt.clf()
    plt.draw()

    time.sleep(5)

# end of code
