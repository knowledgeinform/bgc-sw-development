# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:34:22 2023

@author: moonnt1

Function for FPD Block parameters. This code is to be called from Main_temperature_control 
This code sets up the parameters for FPD Block analog input, control loop, output, and alarms. 

Version 1
"""

# importing required functions
import minimalmodbus


def setup_fpd_block(instrument: minimalmodbus.Instrument, fpd_temp_setting: float) -> None:
    # SetUp for Analog Input 8: Pages 49-50 and 69-73 in RMH manual
    FPD_sen = instrument.write_register(388 + 90 * 7, 95, 0)  # Sensor Type
    FPD_lin = instrument.write_register(390 + 90 * 7, 48, 0)  # TC Linearization
    FPD_unit = instrument.write_register(462 + 90 * 7, 1540, 0)  # Unit
    FPD_display_units = instrument.write_register(368, 15, 0)  # Display Unit
    FPD_display_precision = instrument.write_register(418 + 90 * 7, 40, 0)  # Display Precision

    # Set Up for Control Loop 8: Pages 53-56 and 82-90 in RMH manual
    FPD_CL_source_function_A = instrument.write_register(4156 + 70 * 7, 142, 0)  # Source Function A
    FPD_CL_heat_alg = instrument.write_register(4104 + 70 * 7, 71, 0)  # heat algorithm
    FPD_CL_h_Pb = instrument.write_register(4110 + 70 * 7, 2.00, 0)  # heat proportional band
    FPD_CL_h_hy = instrument.write_register(4120 + 70 * 7, 1.00, 0)  # heat hysteresis
    FPD_Cl_rP = instrument.write_register(5246 + 80 * 7, 88, 0)  # Ramp Action
    FPD_Cl_r_SC = instrument.write_register(5248 + 80 * 7, 57, 0)  # Ramp Scale
    FPD_Cl_r_rt = instrument.write_register(5252 + 80 * 2, 5.00, 2)  # Ramp Rate
    FPD_Cl_C_SP = instrument.write_register(5220 + 80 * 7, fpd_temp_setting, 0)  # set point
    FPD_Cl_id_S = instrument.write_register(5236 + 80 * 7, fpd_temp_setting, 0)  # idle set point
    FPD_Cl_C_m = instrument.write_register(4100 + 70 * 7, 10, 0)  # control loop mode

    # Setup for Output 4 (2A SSR): Pages 82-90 in RMH manual
    FPD_O1_Fn = instrument.write_register(1828 + 30 * 4, 142, 0)  # Function
    FPD_O1_Fi = instrument.write_register(1830 + 30 * 4, 8, 0)  # Function Instance
    FPD_O1_SZ_A = instrument.write_register(1842 + 30 * 4, 1, 0)  # Source Zone
    FPD_O1_o_Ct = instrument.write_register(1822 + 30 * 4, 103, 0)  # Time base Type
    FPD_O1_low = instrument.write_register(1836 + 30 * 4, 0.00, 0)  # Low Scale
    FPD_O1_high = instrument.write_register(1838 + 30 * 4, 100.00, 0)  # High Scale

    # Setup for Alarm 8: Pages 56-58 and 95-99 in RMH manual
    FPD_A1_A_ty = instrument.write_register(2688 + 60 * 7, 24, 0)  # Alarm Type
    FPD_A1_Sr_A = instrument.write_register(2692 + 60 * 7, 142, 0)  # Alarm Source
    FPD_A1_iS_A = instrument.write_register(2694 + 60 * 7, 8, 0)  # Alarm Source Instance
    FPD_A1_SZ_A = instrument.write_register(2708 + 60 * 7, 1, 0)  # Alarm Source Zone
    FPD_A1_Loop = instrument.write_register(2704 + 60 * 7, 8, 0)  # Control Loop
    FPD_A1_A_hy = instrument.write_register(2664 + 60 * 7, 2.00, 0)  # Alarm Hysteresis
    FPD_A1_A_lg = instrument.write_register(2668 + 60 * 7, 17, 0)  # Alarm Logic
    FPD_A1_Sd = instrument.write_register(2666 + 60 * 7, 53, 0)  # Alarm Sides
    FPD_A1_A_Low = instrument.write_register(
        2662 + 60 * 7, 5.00, 0
    )  # Low set point #need to figure out how to make negative
    FPD_A1_A_hi = instrument.write_register(2660 + 60 * 7, 5.00, 0)  # High set point)
    FPD_A1_A_LA = instrument.write_register(2672 + 60 * 7, 60, 0)  # Latching
    FPD_A1_Blocking = instrument.write_register(2674 + 60 * 7, 88, 0)  # Blocking
