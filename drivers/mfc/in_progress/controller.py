"""
Ethan Nguyen APL/AOS-QPT 2023
Controls Alicat BASIS MFCs using command line
Requires BasisMFC.py file
"""
from drivers.mfc.in_progress.serialClient import SerialClient
from drivers.mfc.in_progress.BasisMFC import BASISController

controllerSet = set()


# 12V and .2A
def main():
    client = SerialClient("COM4")
    """
    Available Commands:
    get polling data
    get/set setpoint
    get/set watchdog
    read/set average flow
    set gas
    tarring
    read/change modbus
    read/change baudrate

    Missing Commands due to old firmware:
    auto-tare (manual tare only)
    floating point number setpoints (only ints allowed)
    PID tuning(valve actuation)
    """
    # get_unknown_controller(client)
    control1 = BASISController(client, "B")
    if control1.setup():
        controllerSet.add(control1)
    control2 = BASISController(client, "C")
    if control2.setup():
        controllerSet.add(control2)
    control3 = BASISController(client, "D")
    if control3.setup():
        controllerSet.add(control3)
    control4 = BASISController(client, "E")
    if control4.setup():
        controllerSet.add(control4)
    control5 = BASISController(client, "F")
    if control5.setup():
        controllerSet.add(control5)
    control6 = BASISController(client, "G")
    if control6.setup():
        controllerSet.add(control6)
    control7 = BASISController(client, "H")
    if control7.setup():
        controllerSet.add(control7)
    # get_full_controller_details()
    get_all_controller_states()
    controller_count()
    handle_user_input()


def get_unknown_controller(client):
    # Conenct one controller at a time if response is corrupted
    message = "*"
    client._write(message)
    print(client._readline(), flush=True)
    return client._readline()


def get_full_controller_details():
    for controller in controllerSet:
        print("Controller: " + controller.get(), flush=True)
        print(controller.read_average_flow(), flush=True)
        print(controller.get_watchdog(), flush=True)
        print(controller.read_modbus(), flush=True)
        print(controller.read_baudrate(), flush=True)
        print(controller.query_full_scale(), flush=True)
        print(controller.firmware_version(), flush=True)
        print(controller.serial_number(), flush=True)


def get_all_controller_states():
    for controller in controllerSet:
        print(controller.get(), flush=True)
    return


def controller_count():
    print(str(len(controllerSet)) + " Controller(s) Connected")
    for controller in controllerSet:
        print("Controller " + controller.unitID, flush=True)
    return


def get_controller_state():
    print("Enter Controller ID:", flush=True)
    controllerID = input()
    for controller in controllerSet:
        if controller.unitID.lower() == controllerID.lower():
            if controller.is_open():
                print(controller.get(), flush=True)
                return
            else:
                print("Cannot communicate with Controller: " + controller.unitID)
                return
    print("Controller not found", flush=True)
    return


def change_controller_gas():
    print("Enter Controller ID:", flush=True)
    controllerID = input()
    for controller in controllerSet:
        if controller.unitID.lower() == controllerID.lower():
            if controller.is_open():
                print("Enter Desired Gas:", flush=True)
                gas = input()
                print(controller.change_gas(gas), flush=True)
                return
            else:
                print("Cannot communicate with Controller: " + controller.unitID)
                return
    print("Controller not found", flush=True)
    return


def set_controller_setpoint():
    print("Enter Controller ID:", flush=True)
    controllerID = input()
    for controller in controllerSet:
        if controller.unitID.lower() == controllerID.lower():
            if controller.is_open():
                print("Enter desired Setpoint:", flush=True)
                newSetpoint = input()
                print(controller.set_setpoint(newSetpoint), flush=True)
                return
            else:
                print("Cannot communicate with Controller: " + controller.unitID)
                return
    print("Controller not found", flush=True)
    return


def tare_controllers():
    print("Taring Controllers")
    for controller in controllerSet:
        if controller.is_open():
            print(controller.tarring(), flush=True)
        else:
            print("Cannot communicate with Controller: " + controller.unitID)
    return


def change_controller_modbusID():
    print("Enter Controller ID:", flush=True)
    controllerID = input()
    for controller in controllerSet:
        if controller.unitID.lower() == controllerID.lower():
            if controller.is_open():
                print("Enter desired ModbusID from 1-247:", flush=True)
                newID = input()
                print(controller.change_modbus(newID), flush=True)
                return
            else:
                print("Cannot communicate with Controller: " + controller.unitID)
                return
    print("Controller not found", flush=True)
    return


def average_controller_flow():
    print("Enter Controller ID:", flush=True)
    controllerID = input()
    for controller in controllerSet:
        if controller.unitID.lower() == controllerID.lower():
            if controller.is_open():
                print("Enter desired average from 0-9", flush=True)
                newID = input()
                print(controller.set_average_flow(newID), flush=True)
                return
            else:
                print("Cannot communicate with Controller: " + controller.unitID)
                return
    print("Controller not found", flush=True)
    return


def set_controller_watchdog():
    print("Enter Controller ID:", flush=True)
    controllerID = input()
    for controller in controllerSet:
        if controller.unitID.lower() == controllerID.lower():
            if controller.is_open():
                print("Enter desired time(ms) from 0-5000", flush=True)
                newID = input()
                print(controller.set_watchdog(newID), flush=True)
                return
            else:
                print("Cannot communicate with Controller: " + controller.unitID)
                return
    print("Controller not found", flush=True)
    return


def control_exhaust():
    print("Enter Controller ID:", flush=True)
    controllerID = input()
    for controller in controllerSet:
        if controller.unitID.lower() == controllerID.lower():
            if controller.is_open():
                print("Exhaust?(Y/N)")
                decision = input()
                if decision.lower() == "y":
                    controller.exhaust()
                else:
                    controller.cancel_exhaust()
                return
            else:
                print("Cannot communicate with Controller: " + controller.unitID)
                return
    return


def handle_user_input():
    print("Awaiting input", flush=True)
    data = input()
    while data.lower() != "exit":
        if data.lower().__contains__("list"):
            controller_count()
        elif data.lower().__contains__("state"):
            get_controller_state()
        elif data.lower().__contains__("all"):
            get_all_controller_states()
        elif data.lower().__contains__("setpoint"):
            set_controller_setpoint()
        elif data.lower().__contains__("gas"):
            change_controller_gas()
        elif data.lower().__contains__("tare"):
            tare_controllers()
        elif data.lower().__contains__("modbus"):
            change_controller_modbusID()
        elif data.lower().__contains__("average"):
            average_controller_flow()
        elif data.lower().__contains__("watchdog"):
            set_controller_watchdog()
        elif data.lower().__contains__("exhaust"):
            control_exhaust()
        else:
            print("INVALID COMMAND", flush=True)
        print("Awaiting input", flush=True)
        data = input()
    quit()


if __name__ == "__main__":
    main()
