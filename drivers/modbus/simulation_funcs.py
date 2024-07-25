import datetime
from math import copysign
import random
from typing import Callable, Optional, Tuple, TypeAlias


from drivers.modbus.simulation import SimulatedReadFun, ModbusAddress, SimulatedValues, SimulatedWriteFun, Value

ChangePerSec: TypeAlias = float


def jitter_read(min: float, max: float) -> SimulatedReadFun:
    """
    Create a simulated read function that will always read the last value written +/- rand[min, max]

    Arguments:
        min -- minimum to deviate from written
        max -- maximum value to deviate from written

    Returns:
        simulated read function
    """

    def read(vs: SimulatedValues, i: ModbusAddress) -> Value:
        assert max >= min
        assert isinstance(vs[i], float), f"Attempt to jitter non-float register {i}"
        delta = max - min
        jitter = min + (random.random() * delta)
        return vs[i] + jitter

    return read


def linear_ramp_read_to_write(rate: ChangePerSec) -> Tuple[SimulatedReadFun, SimulatedWriteFun]:
    """
    Create a simulated read/write pair such that:
    * write sets the target value to v
    * read approaches v at rate until it reaches it then stops

    * sim.reads[i], sim.writes[i] = this_func(rate), write[i] causes read [i] to approach value at rate
    * sim.reads[i], sim.writes[j] = this_func(rate), write [j causes read [i] to approach value at rate

    Arguments:
        rate -- positive rate to use to get to v (algorithm goes up/down depending on starting register value)

    Returns:
        Read / Write function pair
    """
    assert rate > 0
    target: float
    written_at: datetime.datetime

    def write(vs: SimulatedValues, i: ModbusAddress, v: float) -> None:
        assert (i not in vs) or isinstance(vs[i], float), f"Attempt to ramp to non-float register {i}"

        nonlocal target, written_at
        written_at = datetime.datetime.now()
        target = v

    def read(vs: SimulatedValues, i: ModbusAddress) -> float:
        assert isinstance(vs[i], float), f"Attempt to ramp to non-float register {i}"

        nonlocal target, written_at

        if i not in vs:
            vs[i] = float()

        delta = target - vs[i]
        time_to = abs(delta) / rate
        now_ = datetime.datetime.now()
        time_since_written = (now_ - written_at).total_seconds()
        if time_since_written > time_to:
            vs[i] = target  # lock at exact target
        else:
            vs[i] += copysign(1, delta) * time_since_written * rate
        written_at = now_
        return vs[i]

    return (read, write)


"""
Need a to simulate turning on a heater and then it heats at some rate R[cool] to a limit.
Then after turning off the heater it cools at some rate R[Cool] to another limit.
Assume we turn on/off with register Heater and read with Temp we would
have
def write[vs, Heater, v]:
    if v = On
        read[Temp] = change_at_linear_rate_funcs(heating_rate, ...)
    if v = Off
        read[Temp] = change_at_linear_rate(funcs(cooling_rate, ...)
"""


def ramp_at_linear_rate(
    rate: ChangePerSec,
    limit: Optional[float] = None,
) -> SimulatedReadFun:
    """
    Create a simulated read that begins changing the current value of a register by rate optionally stopping at some
    limit.

    Arguments:
        rate -- rate to change the current register value by
        limit -- optional limit to limit the register to

    Returns:
        simulated read function
    """

    change_at = datetime.datetime.now()

    clamp: Callable[[float, float], float] = min if rate > 0 else max

    def read(vs: SimulatedValues, i: ModbusAddress) -> float:
        assert isinstance(vs[i], float), f"Attempt to change non-float register {i}"

        nonlocal change_at

        if i not in vs:
            vs[i] = float()

        now_ = datetime.datetime.now()
        time_since_delta = (now_ - change_at).total_seconds()
        vs_i = vs[i]
        adjust = (limit is None) or ((clamp(vs_i, limit)) == vs_i)
        if adjust:
            # we'll be heading the right way, haven't overshot yet or we don't care
            v = vs_i + (time_since_delta * rate)
            vs[i] = clamp(v, limit) if limit is not None else v
        change_at = now_
        return vs[i]

    return read
