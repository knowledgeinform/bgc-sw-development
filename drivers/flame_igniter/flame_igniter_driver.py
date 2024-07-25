import aioserial
import serial
from loguru import logger


class FlameIgniterException(Exception):
    pass


# TODO doesn't seem like we ever close the port in the demos...   what's up
# TODO need to include simulation


class FlameIgniterDriver:
    def __init__(self, port: serial.Serial) -> None:
        """
        Driver for the flame igniter board

        Arguments:
            port -- port to use to communicate with the igniter
        """
        self._port = port

    def _check_response(
        self,
        # TBD is there any expected response we should check other than not ""
    ) -> None:
        response = self._port.readline()
        if response == "":
            error = "No communication with device"
            logger.error(error)
            raise FlameIgniterException(error)

    def turn_on(self) -> None:
        self._port.write("Y".encode("utf-8"))
        self._check_response()

    def turn_off(self) -> None:
        self._port.write("N".encode("utf-8"))
        self._check_response()


class AsyncFlameIgniterDriver:
    def __init__(self, port: aioserial.AioSerial) -> None:
        self._port = port

    async def _check_response(
        self,
        # TBD is there any expected response we should check other than not ""
    ) -> None:
        response = await self._port.readline_async()
        if response == "":
            error = "No communication with device"
            logger.error(error)
            raise FlameIgniterException(error)

    async def turn_on(self) -> None:
        await self._port.write_async("Y".encode("utf-8"))
        await self._check_response()

    async def turn_off(self) -> None:
        await self._port.write_async("N".encode("utf-8"))
        await self._check_response()


if __name__ == "__main__":
    import json
    from time import sleep

    f = open("com_info.json")
    data = json.load(f)
    flame_port = serial.Serial(data["com_assignment"][0]["flame_igniter_port"], 115200)
    f.close

    driver = FlameIgniterDriver(flame_port)
    driver.turn_on()
    sleep(5)
    driver.turn_off()
