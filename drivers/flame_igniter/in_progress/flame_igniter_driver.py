import serial
import json
from loguru import logger


class flame_igniter:
    def _ignition(message) -> bool | None:
        f = open("com_info.json")
        data = json.load(f)
        arduino_data = serial.Serial(data["com_assignment"][0]["flame_igniter_port"], 115200)
        f.close

        if message == "Y":
            arduino_data.write(message.encode("utf-8"))
            response = arduino_data.readline()
            if response == "":
                logger.error("No communication with device")
                return False
            else:
                logger.info("Sent ON command to igniter")
                return True
        if message == "N":
            arduino_data.write(message.encode("utf-8"))
            response = arduino_data.readline()
            if response == "":
                logger.error("No communication with device")
                return False
            else:
                logger.info("Sent ON command to igniter")
                return True
