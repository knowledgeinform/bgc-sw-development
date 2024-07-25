"""
Ethan Nguyen APL/AOS-QPT 2023
Works to send/receive commands from Alicat BASIS OEM MFC Controller
Uses Pyserial package to communicate on COM port using RS-485 communication
Controller.py has command line functions
"""


class BASISController:
    gases = ["Air", "Ar", "CO2", "N2", "O2", "N2O", "H2", "He"]  # Only 8 different gases calibrated

    flow_average = [0, 5, 10, 20, 40, 80, 160, 320, 640, 1280]

    def __init__(self, client, unitID):
        # Variables for initial setup
        self.client = client
        self.unitID = unitID

    def setup(self):
        # set setpoints to save on flash memory change U to D
        command = self.unitID + "ws=D"
        self.client._write(command)
        # clear line by reading
        line = self.client._readline()
        line = self.get()
        if line == "":
            print("Unable to communicate with Controller " + self.unitID)
            return False
        return True

    def is_open(self):
        """
        Check to see if controller can receive/send data
        """
        command = self.unitID
        self.client._write(command)
        line = self.client._readline()
        if line == "":
            return False
        else:
            return True

    def get(self):
        """
        Return Polling Data, read returns a line that is parsed
        """
        command = self.unitID
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def get_setpoint(self):
        command = self.unitID + "rs"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def set_setpoint(self, desiredsetpoint: int):
        """
        Set the target setpoint
        Int value = 4000 * desired setpoint / full scale range
        Old firmware always thinks full scale range is 1000
        Lower ranges will simply be scaled down (i.e. a3040 = 76 on 100 SCCM)
        ex. 760 SCCM = 4000 * 760/1000 = 3040 so 'a3040' would be run
        """
        newsetpoint = 4000 * (int(desiredsetpoint) / 1000)
        command = self.unitID + str(int(newsetpoint))
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def get_watchdog(self):
        """
        raed watchdog time
        """
        command = self.unitID + "rw"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def set_watchdog(self, watchdog):
        """
        Timeout to close valve is no serial communication received
        """
        command = self.unitID + "ww=" + str(int(watchdog))
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def read_average_flow(self):
        """
        Read averaging on unit
        """
        command = self.unitID + "ra"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return "FLOW AVERAGE=" + str(self.flow_average[int(line[4:])]) + "ms"

    def set_average_flow(self, flowValue):
        """
        Govern how smoothing effect, used for rapidly changing flow readings
        """
        command = self.unitID + "wa=" + flowValue
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def change_gas(self, gas):
        """
        change gas using 0-7 or any of gases below
        gas: The gas type, as a string or integer. Supported gases are:
                'Air', 'Ar', 'CO2', 'N2', 'O2', 'N2O', 'H2', 'He'
        """
        if not gas.isdigit():
            if gas in self.gases:
                gasIndex = self.gases.index(gas)
            else:
                return "Gas not supported"
        else:
            gasIndex = gas
        command = self.unitID + "g" + str(gasIndex)
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def tarring(self):
        """
        Tares flow controller, if auto-tare is enabled simply set setpoint of zero for 2 seconds
        Sets zero flow reading, must be done when no flow is passing through the controller
        NO AUTOTARE at current 2.0 firmware
        """
        command = self.unitID + "v"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def change_modbus(self, id):
        """
        Sets modbus/rtu device address from 1-247, default is 1
        """
        command = self.unitID + "wm=" + str(int(id))
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def read_modbus(self):
        """
        Sets modbus/rtu device address from 1-247, default is 1
        """
        command = self.unitID + "rm"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def change_baudrate(self, value):
        """
        Sets baudrate, BASIS units can communicate over bauds rates of 4800, 9600, 19200,
        38400, 57600, or 115200. 38400 is the default baud rate.
        0 - 4800, 1 - 9600, 2 - 19200, 3 - 38400, 4 - 57600, 5 - 115200

        COM PORT will not be able to change in time as it is set to communicate at certain rate
        Must update the serial terminal after change
        """
        if int(value) > 5 or int(value) < 0:
            return "Invalid Value, see table"
        command = self.unitID + "wb=" + str(int(value))
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def read_baudrate(self):
        """
        Reads current baudrate
        """
        command = self.unitID + "rb"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def firmware_version(self):
        """
        Current firmware version of device
        """
        command = self.unitID + "rv"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return "FIRMWARE " + line

    def query_full_scale(self):
        """
        Current firmware version of device
        """
        command = self.unitID + "f"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def serial_number(self):
        """
        Serial Number of device
        """
        command = self.unitID + "rn"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def exhaust(self):
        """
        Exhaust on, state will have additional column that returns EXH
        """
        command = self.unitID + "e"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line

    def cancel_exhaust(self):
        """
        Exhaust off, controller prints out CONTINUE
        """
        command = self.unitID + "c"
        self.client._write(command)
        line = self.client._readline()
        # print(line, flush=True)
        return line
