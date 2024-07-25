# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:37:55 2023

@author: moonnt1

This code was designed as a test script for the Watlow EZ-Zone to control one
heater with one analog input. In addition, a pop-up user interface allows the user
to view the current temperature and read any current errors
"""

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

# SetUp for Analog Input 1

# sensor types: off (62, off set 90), thermocouple (95), millivolts (56), ... see page 69 of manual
sen = instrument.write_register(388, 95, 0)
# TC Linerization (register 390, off set 90): K thermocouple 48
lin = instrument.write_register(390, 48, 0)
# Unit (register 462, off set 90) for temperature analog input should be 1540 for Absolute Temperature
unit = instrument.write_register(462, 1540, 0)
# Display Units (register 368): F (30) or C (15)
display_units = instrument.write_register(368, 15, 0)
# Display Precision (register 418, off set 90): Whole (105), Tenths (94), Hundreths (40), Thousandths(96)
display_precision = instrument.write_register(418, 94, 0)


# Set Up for Control Loop 1

# source function A (register 4156, offset 70) - Analog Input (142)
CL_source_function_A = instrument.write_register(4156, 142, 0)
# heat algorithum (register 4104, offset 70) PID (71)
CL_heat_alg = instrument.write_register(4104, 71)
# cool algorithum (register 4106, offset 70), PID (71)
CL_cool_alg = instrument.write_register(4104, 71)
# Heat propotional band (register 4110, offset 70)
CL_h_Pb = instrument.write_register(4110, 3.00, 2)
# on/off heat hysteries (register 4120, offset 70)
CL_h_hy = instrument.write_register(4120, 1.00, 2)
# cool propotional band (register 4112, offset 70)
CL_c_Pb = instrument.write_register(4112, 3.00, 2)
# on/off cool hysteries (register 4122, offset 70)
CL_c_hy = instrument.write_register(4122, 1.00, 2)
# Ramp Action (register 5246, offset 80): off (62), startup (88), set point change (85), both (13)
Cl_rP = instrument.write_register(5246, 13, 0)
# Ramp Scale (register 5248, offset 80): hours (39), minutes (57)
Cl_r_SC = instrument.write_register(5248, 57, 0)
# Ramp Rate (register 5252, offset 80)
Cl_r_rt = instrument.write_register(5252, 5.00, 2)
# Set Point (register 5220, offset 80)
Cl_C_SP = instrument.write_register(5220, 40.00, 2)
# Idle Set Point (register 5236, offset 80)
Cl_id_S = instrument.write_register(5236, 40.00, 2)
# Control loop mode: (register 4100, offset 70), off (62), auto (10), manual (54)
Cl_C_m = instrument.write_register(4100, 10, 0)

# Set up for Outputs, 2 needed

# Output 1:
# output function (register 1828, offset 30) (see page 91 of manual)
O1_Fn = instrument.write_register(1828, 6, 0)
# output function instance (register 1830, offset 30), can be 1 to 250
O1_Fi = instrument.write_register(1830, 1, 0)
# output souce zone (register 1842, offset 30), can be 0 to 24
O1_SZ_A = instrument.write_register(1842, 0, 0)
# Time base type (register 1822, offset 30) fixed (34), variable (103)
O1_o_Ct = instrument.write_register(1822, 103, 0)

# Output2:
# output function (register 1828, offset 30) (see page 91 of manual)
O2_Fn = instrument.write_register(1858, 6, 0)
# output function instance (register 1830, offset 30), can be 1 to 250
O2_Fi = instrument.write_register(1860, 2, 0)
# output souce zone (register 1842, offset 30), can be 0 to 24
O2_SZ_A = instrument.write_register(1872, 0, 0)
# Time base type (register 1822, offset 30) fixed (34), variable (103)
O2_o_Ct = instrument.write_register(1852, 103, 0)


# Set Up for Alarms
# 1.) Signal  Heater too hot and turn off control loop
# 2.) Signal Heater too cold and turn control loop back on

# Alarm 1
# alarm type (register 2688, offset 60): off (62), process (76), deviation (24)
A1_A_ty = instrument.write_register(2688, 76, 0)
# alarm source (register 2692, offset 60): see page 95
A1_Sr_A = instrument.write_register(2692, 142, 0)
# alarm source instance (register 2694, offset 60) 1 to 250
A1_iS_A = instrument.write_register(2694, 1, 0)
# alarm source zone (register 2708, offset 60), 0 to 24
A1_SZ_A = instrument.write_register(2708, 0, 0)
# control loop (register 2704, offset 60), 1 to 250
A1_Loop = instrument.write_register(2704, 1, 0)
# alarm hysteresis (register 2664, offset 60)
A1_A_hy = instrument.write_register(2664, 1.00, 2)
# alarm logic (register 2668, offset 60): close on alarm (17) or open on alarm (66)
A1_A_lg = instrument.write_register(2668, 17, 0)
# alarm sides (register 266, offset 60): both (13), high (37), low (53)
A1_Sd = instrument.write_register(2666, 53, 0)
# low set point (register 2662, offset 60)
A1_A_Low = instrument.write_register(2662, 37.00, 0)
# highset point (register 2660, offset 60)
A1_A_hi = instrument.write_register(2660, 43.00, 0)
# Alarm latching (register 2672, offset 60): non-latching (60) or latching (49)
A1_A_LA = instrument.write_register(2672, 60, 0)

# Alarm 2
# alarm type (register 2688, offset 60): off (62), process (76), deviation (24)
A2_A_ty = instrument.write_register(2748, 76, 0)
# alarm source (register 2692, offset 60): see page 95
A2_Sr_A = instrument.write_register(2752, 142, 0)
# alarm source instance (register 2694, offset 60) 1 to 250
A2_iS_A = instrument.write_register(2754, 1, 0)
# alarm source zone (register 2708, offset 60), 0 to 24
A2_SZ_A = instrument.write_register(2768, 0, 0)
# control loop (register 2704, offset 60), 1 to 250
A2_Loop = instrument.write_register(2764, 1, 0)
# alarm hysteresis (register 2664, offset 60)
A2_A_hy = instrument.write_register(2724, 1.00, 2)
# alarm logic (register 2668, offset 60): close on alarm (17) or open on alarm (66)
A2_A_lg = instrument.write_register(2728, 66, 0)
# alarm sides (register 2666 offset 60): both (13), high (37), low (53)
A2_Sd = instrument.write_register(2726, 37, 0)
# low set point (register 2662, offset 60)
A2_A_Low = instrument.write_register(2722, 37.00, 0)
# hig set point (register 2660, offset 60)
A2_A_hi = instrument.write_register(2720, 43.00, 0)
# Alarm latching (register 2672, offset 60): non-latching (60) or latching (49)
A2_A_LA = instrument.write_register(2732, 60, 0)


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

    # print(str(CurrentTime) + ' -- ' + str(float(Celsius)))

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

    # reporting any alarms or errors in feed for Analog Input 1, prints status every 5 minutes
    input1_alarm = instrument.read_register(382)
    if input1_alarm == 65:
        print("Analog Input 1: Open")
    elif input1_alarm == 127:
        print("Analog Input 1: Shorted")
    elif input1_alarm == 140:
        print("Analog Input 1: Measurement Error")
    elif input1_alarm == 9:
        print("Analog Input 1: Ambient Error")
    elif input1_alarm == 141:
        print("Analog Input 1: RTD Error")
    elif input1_alarm == 32:
        print("Analog Input 1: Fail")
    elif input1_alarm == 139:
        print("Analog Input 1: Bad calibration Data")
    else:
        print("Analog Input 1: No errors")

    # reporting any alarms or errors in feed for Alarm 1, prints status ever 5 minutes
    alarm1_state = instrument.read_register(2686)
    if alarm1_state == 88:
        print("Alarm 1 Status: Startup")
    elif alarm1_state == 12:
        print("Alarm 1 Status: Blocked")
    elif alarm1_state == 8:
        print("Alarm 1 Status: Alarm Low")
    elif alarm1_state == 7:
        print("Alarm 1 Status: Alarm High")
    elif alarm1_state == 28:
        print("Alarm 1 Status: Error")
    else:
        print("Alarm 1 Status: No Errors")

    # reporting any alarms or errors in feed for Alarm 2, prints status ever 5 minutes
    alarm2_state = instrument.read_register(2686)
    if alarm2_state == 88:
        print("Alarm 2 Status: Startup")
    elif alarm2_state == 12:
        print("Alarm 2 Status: Blocked")
    elif alarm2_state == 8:
        print("Alarm 2 Status: Alarm Low")
    elif alarm2_state == 7:
        print("Alarm 2 Status: Alarm High")
    elif alarm2_state == 28:
        print("Alarm 2 Status: Error")
    else:
        print("Alarm 2 Status: No Errors")

    time.sleep(5)

# end of code
