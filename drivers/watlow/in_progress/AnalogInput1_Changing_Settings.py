# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:36:34 2023

@author: moonnt1
"""

# This code is used to change the basic settings of Input 1 see Watlow EZ-Zone
# Manual (Chapter 3 and 4)for additional options

import minimalmodbus


class WatLow:
    def __init__(self, addr, baudrate):
        self.address = addr
        self.baudrate = baudrate


controller = WatLow(1, 9600)
# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument("COM7", controller.address)
instrument.serial.baudrate = controller.baudrate
# setting up all the standard Analog Input Options for k-type thermocouple

# sensor types: off (62, off set 90), thermocouple (95), millivolts (56), ... see page 69
sen = 95
new_sen1 = instrument.write_register(388, sen, 0)

# TC Linerization (register 390, off set 90): K thermocouple 48
thermo_type = 48
new_lin1 = instrument.write_register(390, thermo_type, 0)

# Unit (register 462, off set 90) for temperature analog input should be 1540 for Absolute Temperature

unit = 1540
new_unit = instrument.write_register(462, unit, 0)

# Display Units (registry 368): F (30) or C (15)
F = 30
C = 15
display_units = instrument.write_register(368, C, 0)
current_display_units = instrument.read_register(368)
print(current_display_units)


# verifying values are correct
current_sen1 = instrument.read_register(388)
print(current_sen1)

current_lin1 = instrument.read_register(390)
print(current_lin1)

current_unit1 = instrument.read_register(462)
print(current_unit1)
