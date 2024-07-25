# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:23:09 2023

@author: moonnt1

Function Code for Valve Oven Zone 1 parameters. This code is to be called from Watlow_MainControl.
This code sets up the parameters for Valve Oven Zone 1 analog input, control loop, output, and alarms. 

Version 1
"""

# importing required functions
import minimalmodbus


def setup_valve_oven_1(instrument: minimalmodbus.Instrument, valve_oven_temp_setting: float) -> None:
    # SetUp for Analog Input 1: Pages 49-50 and 69-73 in RMH manual
    VO1_sen = instrument.write_register(388, 95, 0)  # Sensor Type
    VO1_lin = instrument.write_register(390, 48, 0)  # TC Linerization
    VO1_unit = instrument.write_register(462, 1540, 0)  # Unit
    VO1_display_units = instrument.write_register(368, 15, 0)  # Display Unit
    VO1_display_precision = instrument.write_register(418, 40, 0)  # Display Precision

    # Set Up for Control Loop 1: Pages 53-56 and 82-90 in RMH manual
    VO1_CL_source_function_A = instrument.write_register(4156, 142, 0)  # Source Function A
    VO1_CL_heat_alg = instrument.write_register(4104, 71, 0)  # heat algorithm
    VO1_CL_h_Pb = instrument.write_register(4110, 2.00, 0)  # heat proportional band
    VO1_CL_h_hy = instrument.write_register(4120, 1.00, 0)  # heat hysteresis
    VO1_Cl_rP = instrument.write_register(5246, 88, 0)  # Ramp Action
    VO1_Cl_r_SC = instrument.write_register(5248, 57, 0)  # Ramp Scale
    VO1_Cl_r_rt = instrument.write_register(5252, 5.00, 2)  # Ramp Rate
    VO1_Cl_C_SP = instrument.write_register(5220, valve_oven_temp_setting, 0)  # set point
    VO1_Cl_id_S = instrument.write_register(5236, valve_oven_temp_setting, 0)  # idle set point
    VO1_Cl_C_m = instrument.write_register(4100, 10, 0)  # control loop mode

    # Setup for Output 1 (2A SSR): Pages 82-90 in RMH manual
    VO1_O1_Fn = instrument.write_register(1828, 142, 0)  # Function
    VO1_O1_Fi = instrument.write_register(1830, 1, 0)  # Function Instance
    VO1_O1_SZ_A = instrument.write_register(1842, 1, 0)  # Source Zone
    VO1_O1_o_Ct = instrument.write_register(1822, 103, 0)  # Time base Type
    VO1_O1_low = instrument.write_register(1836, 0.00, 2)  # Low Scale
    VO1_O1_high = instrument.write_register(1838, 100.00, 2)  # High Scale

    # Setup for Alarm 1: Pages 56-58 and 95-99 in RMH manual
    VO1_A1_A_ty = instrument.write_register(2688, 24, 0)  # Alarm Type
    VO1_A1_Sr_A = instrument.write_register(2692, 142, 0)  # Alarm Source
    VO1_A1_iS_A = instrument.write_register(2694, 1, 0)  # Alarm Source Instance
    VO1_A1_SZ_A = instrument.write_register(2708, 1, 0)  # Alarm Source Zone
    VO1_A1_Loop = instrument.write_register(2704, 1, 0)  # Control Loop
    VO1_A1_A_hy = instrument.write_register(2664, 2.00, 2)  # Alarm Hysteresis
    VO1_A1_A_lg = instrument.write_register(2668, 17, 0)  # Alarm Logic
    VO1_A1_Sd = instrument.write_register(2666, 53, 0)  # Alarm Sides
    VO1_A1_A_Low = instrument.write_register(2662, 5.00, 0)  # Low set point #need to figure out how to make negative
    VO1_A1_A_hi = instrument.write_register(2660, 5.00, 0)  # High set point)
    VO1_A1_A_LA = instrument.write_register(2672, 60, 0)  # Latching
    VO1_A1_Blocking = instrument.write_register(2674, 88, 0)  # Blocking
