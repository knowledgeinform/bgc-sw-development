from __future__ import annotations
import asyncio
from dataclasses import dataclass
import random
from typing import Any, Dict, Tuple, TypeAlias, cast


"""
Prototype to show how to fit startup code into FastAPI.  This includes code for
* SystemHwManager for creating hardware drivers associated with the proper underlying ports etc.
* Global _simulate_hw Possible way to incorporate hardware simulation (much more in mms-sw)
* SubsystemController which monitors a collection of hardware.
* FastAPI(lifespan=lifespan) runs our code before / after the application starts receiving events.
* api/xyz/status to try it all out...
"""

# Global indicator of whether we're using simulation or real hardware
# Could be managed in a class which then manages different values for different classes of hardware or supports
# a simulate_all() method to just mark them all for simulation.
#
_simulate_hw = True


class Singleton(type):
    """
    Metaclass to create singleton classes.
    From https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python.

    :Examples:

    >>> class Xyz(metaclass=Singleton):
    >>>    pass
    >>> Xyz() is Xyz
    True
    """

    _instances: Dict[Any, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        # Can't annotate this as a @classmethod or FastAPI use fails...
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class XyzDeviceDriver:
    """
    Device driver for Xyz hardware.
    """

    @dataclass
    class Status:
        id: Any = 0
        y: float = 0

    def __init__(self, id: Any, hw_resource: Any):
        self._id = id
        self._hw_resource = hw_resource
        if not _simulate_hw:
            # attach to hardware resource
            raise NotImplementedError(f"{self.__class__.__name__} has no hardware")
        else:
            # prepare simulation
            self._sim_status_seconds = 0.1
            self._sim_y = float(hash(id))  # type: ignore

    @property
    async def status(self) -> Status:
        if not _simulate_hw:
            # asynchronously use the self._hw_resource to get status
            raise NotImplementedError(f"{self.__class__.__name__} has no hardware")
        else:
            # simulate the hardware - possibly changing results around some setpoint
            await asyncio.sleep(self._sim_status_seconds)
            self._sim_y += 0.1 if random.randint(0, 1) else -0.1  # randomly walk around start
            return self.Status(id=self._id, y=self._sim_y)


class SystemHwManager(metaclass=Singleton):
    """
    Singleton class to provide access to all hardware devices (things we create drivers for).
    Responsible for creating all hardware devices and associating them with the proper underlying ports (shared if need
    be), etc.
    This is also probably where external hardware information such as required device IDs, etc. would be used for
    system device mapping.
    Should potentially include Clarity also.
    Based off of mms PowerBoard.*
    """

    def __init__(self) -> None:
        # just as an example, we're managing two instances of an Xyz, like  the 8 MFCs or what-not
        self._xyzs = (
            XyzDeviceDriver(id=1, hw_resource="resource1"),
            XyzDeviceDriver(id=2, hw_resource="resource2"),
        )

    @property
    def xyzs(self) -> Tuple[XyzDeviceDriver, ...]:
        """
        Provide access to the xyz.
        """
        return self._xyzs


SubsystemControllerStatus: TypeAlias = Tuple[XyzDeviceDriver.Status, XyzDeviceDriver.Status]


class SubsystemController(metaclass=Singleton):
    """
    Singleton to manage a set of hardware associated with some subsystem.
    Includes asynchronous periodic monitoring to decouple GUI HW requests from hardware state management.
    Modeled after mms-sw AerosolControl.*
    """

    def __init__(self) -> None:
        self._running = False
        self._xyzs = SystemHwManager().xyzs

        # NOTE: as long as we don't update this piecemeal w/async calls to various HW we don't need any synchronization
        self._status: SubsystemControllerStatus = (
            XyzDeviceDriver.Status(),
            XyzDeviceDriver.Status(),
        )

    async def enable_monitoring(self, enable: bool) -> None:
        if enable:
            self._running = True
            # TBD do we need some extra care to avoid any possibility of weirdness?
            asyncio.create_task(self._monitor())
        else:
            self._running = False

    async def status(self) -> Tuple[XyzDeviceDriver.Status, ...]:
        return self._status

    async def _monitor(self) -> None:
        name = f"{self.__class__.__name__}::{self._monitor.__name__}()"
        print(f"Entering {name}")
        while self._running:
            result = tuple(await asyncio.gather(self._xyzs[0].status, self._xyzs[1].status))
            self._status = cast(SubsystemControllerStatus, result)
            await asyncio.sleep(1)
        print(f"Exiting {name}...")
