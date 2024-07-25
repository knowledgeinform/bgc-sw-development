# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 14:32:11 2023

@author: moonnt1

Main code for BGC Watlow temperature control.

Version 2

Main functions: establish communication with device, temperature inputs, runs functions
to set up. 
"""

# importing required functions
import minimalmodbus
from drivers.watlow.in_progress.Valve_Oven_1 import setup_valve_oven_1
from drivers.watlow.in_progress.Valve_Oven_2A import setup_valve_oven_2A
from drivers.watlow.in_progress.Valve_Oven_2B import setup_valve_oven_2B
from drivers.watlow.in_progress.Valve_Oven_3 import setup_valve_oven_3
from drivers.watlow.in_progress.FPD_Block import setup_fpd_block
# from drivers.watlow.in_progress.Column_Transfer_In import setup_columnxfer_in


# establishing communication with Watlow
class WatLow:
    def __init__(self, addr: int, baudrate: int) -> None:
        self.address = addr
        self.baudrate = baudrate


# Communicating to Watlow EZ-Zone
controller = WatLow(1, 38400)
# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument("COM7", controller.address)
assert instrument.serial is not None
instrument.serial.baudrate = controller.baudrate

# getting user input for temperature settings
valve_oven_temp_setting = float(input("Enter Desired Temperature for Valve Oven Zones (Celsius):"))
fpd_temp_setting = float(input("Enter Desired Temperature for FPD Block (Celsius):"))
# sampleline1_temp_setting = float(input("Enter Desired Temperature for Sample Line 1 (Celsius):"))
# sampleline2_temp_setting = float(input("Enter Desired Temperature for Sample Line 2 (Celsius):"))
# columnxfer_temp_setting = float(input("Enter Desired Temperature for Columns Transfers (Celsius):"))


# verifying that temp settings were not over maximum limits
if valve_oven_temp_setting > 250.00:
    valve_oven_temp_setting = 250.00
    print("Input value over maximum limit for Valve Ovens. Temperature set to maximum limit of 250\N{Degree Sign}C.")

if fpd_temp_setting > 200.00:
    fpd_temp_setting = 200.00
    print("Input value over maximum limit for FPD Block. Temperature set to maximum limit of 200\N{Degree Sign}C.")

# if sampleline1_temp_setting > 180.00:
# sampleline1_temp_setting = 180.00
# print("Input value over maximum limit for Sample Line 1. Temperature set to maximum limit of 180\N{Degree Sign}C.")

# if sampleline2_temp_setting > 150.00:
# sampleline2_temp_setting = 150.00
# print("Input value over maximum limit for Sample Line 2. Temperature set to maximum limit of 150\N{Degree Sign}C.")

# if columnxfer_temp_setting > 280.00:
# columnxfer_temp_setting > 280.00
# print("Input value over maximum limit for Column Transfer zones. Temperature set to maximum limit of 250\N{Degree Sign}C.")

# running the other scripts
setup_valve_oven_1(instrument, valve_oven_temp_setting)
setup_valve_oven_2A(instrument, valve_oven_temp_setting)
setup_valve_oven_2B(instrument, valve_oven_temp_setting)
setup_valve_oven_3(instrument, valve_oven_temp_setting)
setup_fpd_block(instrument, fpd_temp_setting)
# setup_columnxfer_in(instrument, columnxfer_temp_setting)
