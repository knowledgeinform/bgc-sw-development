import time
import pytest
from pymodbus.constants import Endian
from drivers.modbus.base_classes import AsyncModbusBase, ModbusBase

from drivers.modbus.simulation import AsyncSimulatedModbus, ModbusAddress, SimulatedModbus, SimulatedValues
from drivers.modbus.simulation_funcs import ramp_at_linear_rate, jitter_read, linear_ramp_read_to_write


@pytest.fixture
def uut() -> ModbusBase:
    return SimulatedModbus(Endian.BIG, Endian.LITTLE)


@pytest.fixture
def async_uut() -> AsyncModbusBase:
    return AsyncSimulatedModbus(Endian.BIG, Endian.LITTLE)


def test_read_defaults(uut: SimulatedModbus) -> None:
    float_ = uut.read_holding_register_float(address=18)
    assert isinstance(float_, float)
    assert float_ == float()

    int_ = uut.read_holding_register_u16(address=20)
    assert isinstance(int_, int)
    assert int_ == int()


def test_write_wo_read(uut: SimulatedModbus) -> None:
    uut.write_register_float(27, 19.3)
    assert 19.29 < uut.read_holding_register_float(27) < 19.31
    assert uut.read_holding_register_float(18) == 0.0

    uut.write_register_u16(19, 73)
    assert uut.read_holding_register_u16(19) == 73
    assert uut.read_holding_register_u16(2019) == 0


def test_type_fixed_after_1st_access(uut: ModbusBase) -> None:
    # type fixed on read, subsequence wrong type access fail
    register = 20
    uut.read_holding_register_u16(register)
    with pytest.raises(Exception):
        uut.read_holding_register_float(register)
    with pytest.raises(Exception):
        uut.write_register_float(register, 19.3)
    uut.read_holding_register_u16(register)

    register += 2
    uut.read_holding_register_float(register)
    with pytest.raises(Exception):
        uut.read_holding_register_u16(register)
    with pytest.raises(Exception):
        uut.write_register_u16(register, 19)
    uut.read_holding_register_float(register)

    # type fixed on write, subsequence wrong type access fail
    register += 2
    uut.write_register_u16(register, 10)
    with pytest.raises(Exception):
        uut.read_holding_register_float(register)
    with pytest.raises(Exception):
        uut.write_register_float(register, 19.3)
    uut.read_holding_register_u16(register)

    register += 2
    uut.write_register_float(register, 10.0)
    with pytest.raises(Exception):
        uut.read_holding_register_u16(register)
    with pytest.raises(Exception):
        uut.write_register_u16(register, 19)
    uut.read_holding_register_float(register)


def test_read_func(uut: SimulatedModbus) -> None:
    assert isinstance(uut, SimulatedModbus)

    register = 20
    uut.write_register_u16(register, 10)
    uut.write_register_u16(register + 1, 11)
    assert uut.read_holding_register_u16(register) == 10
    assert uut.read_holding_register_u16(register + 1) == 11

    def read_plus_2(vs: SimulatedValues, address: ModbusAddress) -> int:
        result = vs[address]
        assert isinstance(result, int)
        return result + 2

    uut.set_read_fs((register, read_plus_2))
    assert uut.read_holding_register_u16(register) == 10 + 2
    assert uut.read_holding_register_u16(register + 1) == 11

    def read_plus_4(vs: SimulatedValues, address: ModbusAddress) -> int:
        result = vs[address]
        assert isinstance(result, int)
        return result + 4

    uut.set_read_fs((register, read_plus_4))
    assert uut.read_holding_register_u16(register) == 10 + 4
    assert uut.read_holding_register_u16(register + 1) == 11


def test_write_func(uut: SimulatedModbus) -> None:
    assert isinstance(uut, SimulatedModbus)

    register = 20
    uut.write_register_u16(register, 10)
    uut.write_register_u16(register + 1, 11)
    assert uut.read_holding_register_u16(register) == 10
    assert uut.read_holding_register_u16(register + 1) == 11

    def write_plus_2(vs: SimulatedValues, address: ModbusAddress, value: int | float) -> None:
        vs[address] = value + 2

    uut.set_write_fs((register, write_plus_2))
    uut.write_register_u16(register, 10)
    assert uut.read_holding_register_u16(register) == 10 + 2
    uut.write_register_u16(register + 1, 11)
    assert uut.read_holding_register_u16(register + 1) == 11

    def write_plus_4(vs: SimulatedValues, address: ModbusAddress, value: int | float) -> None:
        vs[address] = value + 4

    uut.set_write_fs((register, write_plus_4))
    uut.write_register_u16(register, 10)
    assert uut.read_holding_register_u16(register) == 10 + 4
    uut.write_register_u16(register + 1, 11)
    assert uut.read_holding_register_u16(register + 1) == 11


def test_jitter_read(uut: SimulatedModbus) -> None:
    assert isinstance(uut, SimulatedModbus)

    register = 20
    uut.write_register_float(register, 10.0)
    uut.set_read_fs((register, jitter_read(min=-0.1, max=0.1)))

    values = [uut.read_holding_register_float(register) for x in range(100)]
    for value in values:
        assert (10 - 0.1001) <= value <= (10 + 0.1001)

    average = sum(values) / len(values)
    assert average != 10.0


def test_linear_ramp_to_value_funcs(uut: SimulatedModbus) -> None:
    assert isinstance(uut, SimulatedModbus)

    # up

    register = 20
    read_f, write_f = linear_ramp_read_to_write(1.0)
    uut.set_read_write_fs((register, read_f, write_f))

    uut.write_register_float(register, 0.4)
    time.sleep(0.1)
    value = uut.read_holding_register_float(register)
    assert 0.09 < value < 0.11  # approaching limit

    time.sleep(0.2)
    value = uut.read_holding_register_float(register)
    assert 0.29 < value < 0.31  # approaching limit

    time.sleep(0.2)
    value = uut.read_holding_register_float(register)
    assert 0.399 < value < 0.401  # should be at limit

    # down
    uut.write_register_float(register, 0.2)

    time.sleep(0.1)
    value = uut.read_holding_register_float(register)
    assert 0.29 < value < 0.31  # approaching limit

    time.sleep(0.2)
    value = uut.read_holding_register_float(register)
    assert 0.199 < value < 0.201  # should be at limit


def test_change_at_linear_rate(uut: SimulatedModbus) -> None:
    assert isinstance(uut, SimulatedModbus)

    # up w/o limit

    register = 20
    read_f = ramp_at_linear_rate(1.0)
    uut.set_read_fs((register, read_f))

    uut.write_register_float(register, 0.8)
    value = uut.read_holding_register_float(register)
    assert 0.799 < value < 0.801

    time.sleep(0.1)
    value = uut.read_holding_register_float(register)
    assert 0.89 < value < 0.91

    time.sleep(0.1)
    value = uut.read_holding_register_float(register)
    assert 0.99 < value < 1.01

    # down to limit
    uut.set_read_fs((register, ramp_at_linear_rate(-1.0, limit=0.9)))
    time.sleep(0.1)
    value = uut.read_holding_register_float(register)
    assert 0.89 < value < 0.91

    time.sleep(0.1)
    value = uut.read_holding_register_float(register)
    assert 0.899 < value < 0.91

    # up past limit

    uut.set_read_fs((register, ramp_at_linear_rate(1.0, limit=0.7)))
    time.sleep(0.1)
    value = uut.read_holding_register_float(register)
    assert 0.89 < value < 0.91
