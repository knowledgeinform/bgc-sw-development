# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:01:09 2023

@author: moonnt1

Subcode for Column Xfer In parameters. This code is to be called from Main_temperature_control 
This code sets up the parameters for Column Xfer In analog input, contorl loop, output, and alarms. 

Version 1
"""

# importing required functions
import minimalmodbus


def setup_columnxfer_in(instrument: minimalmodbus.Instrument, columnxfer_temp_setting: float) -> None:
    # SetUp for Analog Input 5: Pages 49-50 and 69-73 in RMH manual
    Xfer_In_sen = instrument.write_register(388 + 90 * 5, 95, 0)  # Sensor Type
    Xfer_In_lin = instrument.write_register(390 + 90 * 5, 48, 0)  # TC Linerization
    Xfer_In_unit = instrument.write_register(462 + 90 * 5, 1540, 0)  # Unit
    Xfer_In_display_units = instrument.write_register(368, 15, 0)  # Display Unit
    Xfer_In_display_precision = instrument.write_register(418 + 90 * 2, 40, 0)  # Display Precision

    # Setup for Alarm 1: Pages 74-78 in RME manual
    Xfer_In_A_Blocking = instrument.write_register(1454, 88, 0)  # Blocking
    Xfer_In_A_Latching = instrument.write_register_(1452, 60, 0)  # ALarm Latching
    Xfer_In_A_Low_Set = instrument.write_register(1442, columnxfer_temp_setting - 5, 2)  # Alarm Low Set Point
    Xfer_In_A_High_Set = instrument.write_register(1440, columnxfer_temp_setting + 5, 2)  # Alarm High Set Point
    Xfer_In_A_Type = instrument.write_register(1468, 76, 0)  # Alarm Type
    Xfer_In_A_Source = instrument.write_register(1472, 142, 0)  # Alarm Source
    Xfer_In_A_Instance = instrument.write_register(1474, 6, 0)  # Alarm Source Instance
    Xfer_In_A_Zone = instrument.write_register(1488, 1, 0)  # Alarm Source Logic
    Xfer_In_A_Hysteresis = instrument.write_register(1444, 1.00, 2)  # Alarm Hysteresis
    Xfer_In_A_Logic = instrument.write_register(1448, 66, 0)  # Alarm Logic
    Xfer_In_A_Sides = instrument.write_register(1446, 53, 0)  # Alarm Sides

    # Setup for output D I/O 1: Pages 44, 63-66, and 69-74 in RME manual
    Xfer_In_O_direction = instrument.write_register(360, 68, 0)  # Digital I/O direction
    Xfer_In_O_Function = instrument.write_register(368, 6, 0)  # Digital I/O Function
    Xfer_In_O_FI = instrument.write_register(370, 6, 0)  # Digital I/O Function Instance
    Xfer_In_O_Zone = instrument.write_register(382, 1, 0)  # Digital Output: Output Source Zone
    Xfer_In_O_Time = instrument.write_register(362, 103, 0)  # Digital Output Time base Type
    Xfer_In_O_Low_P = instrument.write_register(376, 0.00, 2)  # Low Power Scale
    Xfer_In_O_High_P = instrument.write_register(378, 100.00, 2)  # High Power Scale
    Xfer_In_O_Type = instrument.write_register(6990, 104, 2)  # Output Process Type
    Xfer_In_O_Process = instrument.write_register(6992, 142, 0)  # Output Process Function
    Xfer_In_O_instance = instrument.write_register(6996, 6, 0)  # Output Process Function Instance
    Xfer_In_O_Pzone = instrument.write_register(7026, 1, 0)  # Output Process Source Zone
