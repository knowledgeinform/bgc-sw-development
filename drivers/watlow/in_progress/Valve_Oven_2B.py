# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:50:58 2023

@author: moonnt1

Function for Valve Oven Zone 2B parameters. This code is to be called from Watlow_MainControl 
This code sets up the parameters for Valve Oven Zone 1 analog input, control loop, output, and alarms. 

Version 1
"""

# importing required functions
import minimalmodbus


def setup_valve_oven_2B(instrument: minimalmodbus.Instrument, valve_oven_temp_setting: float) -> None:
    VO2B_sen = instrument.write_register(388 + 90 * 2, 95, 0)  # Sensor Type
    VO2B_lin = instrument.write_register(390 + 90 * 2, 48, 0)  # TC Linearization
    VO2B_unit = instrument.write_register(462 + 90 * 2, 1540, 0)  # Unit
    VO2B_display_units = instrument.write_register(368, 15, 0)  # Display Unit
    VO2B_display_precision = instrument.write_register(418 + 90 * 2, 40, 0)  # Display Precision

    # Set Up for Control Loop 2
    VO2B_CL_source_function_A = instrument.write_register(4156 + 70 * 2, 142, 0)  # Source Function A
    VO2B_CL_heat_alg = instrument.write_register(4104 + 70 * 2, 71, 0)  # heat algorithm
    VO2B_CL_h_Pb = instrument.write_register(4110 + 70 * 2, 2.00, 0)  # heat proportional band
    VO2B_CL_h_hy = instrument.write_register(4120 + 70 * 2, 1.00, 0)  # heat hysteresis
    VO2B_Cl_rP = instrument.write_register(5246 + 80 * 2, 88, 0)  # Ramp Action
    VO2B_Cl_r_SC = instrument.write_register(5248 + 80 * 2, 57, 0)  # Ramp Scale
    VO2B_Cl_r_rt = instrument.write_register(5252 + 80 * 2, 5.00, 0)  # Ramp Rate
    VO2B_Cl_C_SP = instrument.write_register(5220 + 80 * 2, valve_oven_temp_setting, 0)  # set point
    VO2B_Cl_id_S = instrument.write_register(5236 + 80 * 2, valve_oven_temp_setting, 0)  # idle set point
    VO2B_Cl_C_m = instrument.write_register(4100 + 70 * 2, 10, 0)  # control loop mode

    # Setup for Output:
    VO2B_O1_Fn = instrument.write_register(1828 + 30 * 2, 142, 0)  # Function
    VO2B_O1_Fi = instrument.write_register(1830 + 30 * 2, 3, 0)  # Function Instance
    VO2B_O1_SZ_A = instrument.write_register(1842 + 30 * 2, 1, 0)  # Source Zone
    VO2B_O1_o_Ct = instrument.write_register(1822 + 30 * 2, 103, 0)  # Time base Type
    VO2B_O1_low = instrument.write_register(1836 + 30 * 2, 0.00, 0)  # Low Scale
    VO2B_O1_high = instrument.write_register(1838 + 30 * 2, 100.00, 0)  # High Scale

    # Setup for Alarm
    VO2B_A1_A_ty = instrument.write_register(2688 + 60 * 2, 24, 0)  # Alarm Type
    VO2B_A1_Sr_A = instrument.write_register(2692 + 60 * 2, 142, 0)  # Alarm Source
    VO2B_A1_iS_A = instrument.write_register(2694 + 60 * 2, 3, 0)  # Alarm Source Instance
    VO2B_A1_SZ_A = instrument.write_register(2708 + 60 * 2, 1, 0)  # Alarm Source Zone
    VO2B_A1_Loop = instrument.write_register(2704 + 60 * 2, 3, 0)  # Control Loop
    VO2B_A1_A_hy = instrument.write_register(2664 + 60 * 2, 2.00, 0)  # Alarm Hysteresis
    VO2B_A1_A_lg = instrument.write_register(2668 + 60 * 2, 17, 0)  # Alarm Logic
    VO2B_A1_Sd = instrument.write_register(2666 + 60 * 2, 53, 0)  # Alarm Sides
    VO2B_A1_A_Low = instrument.write_register(
        2662 + 60 * 2, 5.00, 0
    )  # Low set point #need to figure out how to make negative
    VO2B_A1_A_hi = instrument.write_register(2660 + 60 * 2, 5.00, 0)  # High set point)
    VO2B_A1_A_LA = instrument.write_register(2672 + 60 * 2, 60, 0)  # Latching
    VO2B_A1_Blocking = instrument.write_register(2674 + 60 * 2, 88, 0)  # Blocking
