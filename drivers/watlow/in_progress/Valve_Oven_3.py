# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:43:16 2023

@author: moonnt1

Function for Valve Oven Zone 3 parameters. This code is to be called from Watlow_MainControl 
This code sets up the parameters for Valve Oven Zone 3 analog input, control loop, output, and alarms. 

Version 1
"""

# importing required functions
import minimalmodbus


def setup_valve_oven_3(instrument: minimalmodbus.Instrument, valve_oven_temp_setting: float) -> None:
    # Set up for Analog Input 4: Page 49-50 and 69-70 in RMH manual
    VO3_sen = instrument.write_register(388 + 90 * 3, 95, 0)  # Sensor Type
    VO3_lin = instrument.write_register(390 + 90 * 3, 48, 0)  # TC Linearization
    VO3_unit = instrument.write_register(462 + 90 * 3, 1540, 0)  # Unit
    VO3_display_units = instrument.write_register(368, 15, 0)  # Display Unit
    VO3_display_precision = instrument.write_register(418 + 90 * 2, 40, 0)  # Display Precision

    # Set Up for Control Loop 4: Pages 53-56 and 82-90 in RMH manual
    VO3_CL_source_function_A = instrument.write_register(4156 + 70 * 3, 142, 0)  # Source Function A
    VO3_CL_heat_alg = instrument.write_register(4104 + 70 * 3, 71, 0)  # heat algorithm
    VO3_CL_h_Pb = instrument.write_register(4110 + 70 * 3, 2.00, 0)  # heat proportional band
    VO3_CL_h_hy = instrument.write_register(4120 + 70 * 3, 1.00, 0)  # heat hysteresis
    VO3_Cl_rP = instrument.write_register(5246 + 80 * 3, 88, 0)  # Ramp Action
    VO3_Cl_r_SC = instrument.write_register(5248 + 80 * 3, 57, 0)  # Ramp Scale
    VO3_Cl_r_rt = instrument.write_register(5252 + 80 * 3, 5.00, 2)  # Ramp Rate
    VO3_Cl_C_SP = instrument.write_register(5220 + 80 * 3, valve_oven_temp_setting, 2)  # set point
    VO3_Cl_id_S = instrument.write_register(5236 + 80 * 3, valve_oven_temp_setting, 2)  # idle set point
    VO3_Cl_C_m = instrument.write_register(4100 + 80 * 3, 10, 0)  # control loop mode

    # Setup for Output 3 (2A SSR): Pages 82-90 in RMH manual
    VO3_O1_Fn = instrument.write_register(1828 + 30 * 3, 142, 0)  # Function
    VO3_O1_Fi = instrument.write_register(1830 + 30 * 3, 4, 0)  # Function Instance
    VO3_O1_SZ_A = instrument.write_register(1842 + 30 * 3, 1, 0)  # Source Zone
    VO3_O1_o_Ct = instrument.write_register(1822 + 30 * 3, 103, 0)  # Time base Type
    VO3_O1_low = instrument.write_register(1836 + 30 * 3, 0.00, 2)  # Low Scale
    VO3_O1_high = instrument.write_register(1838 + 30 * 3, 100.00, 0)  # High Scale

    # Setup for Alarm 3: Pages 56-58 and 95-99 in RMH manual
    VO3_A1_A_ty = instrument.write_register(2688 + 60 * 3, 24, 0)  # Alarm Type
    VO3_A1_Sr_A = instrument.write_register(2692 + 60 * 3, 142, 0)  # Alarm Source
    VO3_A1_iS_A = instrument.write_register(2694 + 60 * 3, 4, 0)  # Alarm Source Instance
    VO3_A1_SZ_A = instrument.write_register(2708 + 60 * 3, 1, 0)  # Alarm Source Zone
    VO3_A1_Loop = instrument.write_register(2704 + 60 * 3, 4, 0)  # Control Loop
    VO3_A1_A_hy = instrument.write_register(2664 + 60 * 3, 2.00, 0)  # Alarm Hysteresis
    VO3_A1_A_lg = instrument.write_register(2668 + 60 * 3, 17, 0)  # Alarm Logic
    VO3_A1_Sd = instrument.write_register(2666 + 60 * 3, 53, 0)  # Alarm Sides
    VO3_A1_A_Low = instrument.write_register(
        2662 + 60 * 3, 5.00, 0
    )  # Low set point #need to figure out how to make negative
    VO3_A1_A_hi = instrument.write_register(2660 + 60 * 3, 5.00, 0)  # High set point)
    VO3_A1_A_LA = instrument.write_register(2672 + 60 * 3, 60, 0)  # Latching
    VO3_A1_Blocking = instrument.write_register(2674 + 60 * 3, 88, 0)  # Blocking
