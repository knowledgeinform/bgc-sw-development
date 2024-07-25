from typing import Union

import serial


class SerialClient:
    """Client using a directly-connected RS232 serial device."""

    def __init__(
        self,
        address: str,
        baudrate: int = 38400,
        timeout: float = 0.15,
        bytesize: int = serial.EIGHTBITS,
        stopbits: Union[float, int] = serial.STOPBITS_ONE,
        parity: str = serial.PARITY_NONE,
    ):
        """Initialize serial port."""
        self.address = address
        assert isinstance(self.address, str)
        self.serial_details = {
            "baudrate": baudrate,
            "bytesize": bytesize,
            "stopbits": stopbits,
            "parity": parity,
            "timeout": timeout,
        }
        self.ser = serial.Serial(self.address, **self.serial_details)  # type: ignore [arg-type]

    def _read(self, length: int) -> str:
        """Read a fixed number of bytes from the device."""
        return self.ser.read(length).decode()

    def _readline(self) -> str:
        """Read until a LF terminator."""
        # return self.ser.read_until(b"\r").strip().decode()
        return self.ser.readline().strip().decode()

    def _write(self, message: str) -> None:
        """Write a message to the device."""
        message += "\r\n"
        self.ser.write(message.encode())

    def close(self) -> None:
        """Release resources."""
        self.ser.close()

    def _handle_connection(self) -> None:
        self.open = True
