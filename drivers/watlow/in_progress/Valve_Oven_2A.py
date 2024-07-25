# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:50:58 2023

@author: moonnt1

Function Code for Valve Oven Zone 2A parameters. This code is to be called from Watlow_MainControl 
This code sets up the parameters for Valve Oven Zone 1 analog input, control loop, output, and alarms. 

Version 1
"""

# importing required functions
import minimalmodbus


def setup_valve_oven_2A(instrument: minimalmodbus.Instrument, valve_oven_temp_setting: float) -> None:
    # Set Up for Analog Input 2: Pages 49-50 and 69-73 in RMH manual
    VO2A_sen = instrument.write_register(388 + 90, 95, 0)  # Sensor Type
    VO2A_lin = instrument.write_register(390 + 90, 48, 0)  # TC Linearization
    VO2A_unit = instrument.write_register(462 + 90, 1540, 0)  # Unit
    VO2A_display_units = instrument.write_register(368, 15, 0)  # Display Unit
    VO2A_display_precision = instrument.write_register(418 + 90, 40, 0)  # Display Precision

    # Set Up for Control Loop 2: Pages 53-56 and 82-90 in RMH manual
    VO2A_CL_source_function_A = instrument.write_register(4156 + 70, 142, 0)  # Source Function A
    VO2A_CL_heat_alg = instrument.write_register(4104 + 70, 71, 0)  # heat algorithm
    VO2A_CL_h_Pb = instrument.write_register(4110 + 70, 2.00, 0)  # heat proportional band
    VO2A_CL_h_hy = instrument.write_register(4120 + 70, 1.00, 0)  # heat hysteresis
    VO2A_Cl_rP = instrument.write_register(5246 + 80, 88, 0)  # Ramp Action
    VO2A_Cl_r_SC = instrument.write_register(5248 + 80, 57, 0)  # Ramp Scale
    VO2A_Cl_r_rt = instrument.write_register(5252 + 80, 5.00, 2)  # Ramp Rate
    VO2A_Cl_C_SP = instrument.write_register(5220 + 80, valve_oven_temp_setting, 0)  # set point
    VO2A_Cl_id_S = instrument.write_register(5236 + 80, valve_oven_temp_setting, 0)  # idle set point
    VO2A_Cl_C_m = instrument.write_register(4100 + 70, 10, 0)  # control loop mode

    # Setup for Output 2 (2A SSR): Pages 82-90 in RMH manual
    VO2A_O1_Fn = instrument.write_register(1828 + 30, 142, 0)  # Function
    VO2A_O1_Fi = instrument.write_register(1830 + 30, 2, 0)  # Function Instance
    VO2A_O1_SZ_A = instrument.write_register(1842 + 30, 1, 0)  # Source Zone
    VO2A_O1_o_Ct = instrument.write_register(1822 + 30, 103, 0)  # Time base Type
    VO2A_O1_low = instrument.write_register(1836 + 30, 0.00, 0)  # Low Scale
    VO2A_O1_high = instrument.write_register(1838 + 30, 100.00, 0)  # High Scale

    # Setup for Alarm 2: Pages 56-58 and 95-99 in RMH manual
    VO2A_A1_A_ty = instrument.write_register(2688 + 60, 24, 0)  # Alarm Type
    VO2A_A1_Sr_A = instrument.write_register(2692 + 60, 142, 0)  # Alarm Source
    VO2A_A1_iS_A = instrument.write_register(2694 + 60, 2, 0)  # Alarm Source Instance
    VO2A_A1_SZ_A = instrument.write_register(2708 + 60, 1, 0)  # Alarm Source Zone
    VO2A_A1_Loop = instrument.write_register(2704 + 60, 2, 0)  # Control Loop
    VO2A_A1_A_hy = instrument.write_register(2664 + 60, 2.00, 2)  # Alarm Hysteresis
    VO2A_A1_A_lg = instrument.write_register(2668 + 60, 17, 0)  # Alarm Logic
    VO2A_A1_Sd = instrument.write_register(2666 + 60, 53, 0)  # Alarm Sides
    VO2A_A1_A_Low = instrument.write_register(
        2662 + 60, 5.00, 0
    )  # Low set point #need to figure out how to make negative
    VO2A_A1_A_hi = instrument.write_register(2660 + 60, 5.00, 0)  # High set point)
    VO2A_A1_A_LA = instrument.write_register(2672 + 60, 60, 0)  # Latching
    VO2A_A1_Blocking = instrument.write_register(2674 + 60, 88, 0)  # Blocking
