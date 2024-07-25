# This module contains types used throughout many of the REST APIs.
# Most if not all of these types would provide data validation via pydantic.

from enum import Enum
from pydantic import BaseModel, Field


from typing import Final, Generic, TypeAlias, TypeVar

from server.app.core.device_info import (
    FlowName,
    IsocraticFlowName,
    IsocraticTemperatureName,
    TemperatureName,
)

_NameT = TypeVar("_NameT")
_ValueT = TypeVar("_ValueT")


class _NameValuePair(BaseModel, Generic[_NameT, _ValueT]):
    """
    Same as below but avoids problems with BaseModel.__init__() if constructing a NameValuePair directly
    and not using a TypeAlias.
    """

    name: _NameT = Field(description="Logical device name")
    value: _ValueT


class NameValuePair(_NameValuePair[_NameT, _ValueT], Generic[_NameT, _ValueT]):
    """
    Generic name value pair to associated logical device names with their values
    see https://docs.pydantic.dev/2.0/usage/models/#generic-models

    NOTE: Enums are good _NameT types but so are Literals per https://docs.pydantic.dev/2.5/concepts/performance/.
    Don't use literals though if it's going to cause us to duplicate code.

    :param Generic: Type defining the legal names.
    :type Generic: _NameT
    :param Generic: Type defining the legal values.
    :type Generic: _ValueT
    """

    pass


class Value(BaseModel, Generic[_ValueT]):
    value: _ValueT


class OnOff(str, Enum):
    ON = "on"
    OFF = "off"


TemperaturePair = NameValuePair[TemperatureName, float]

IsocraticTemperaturePair: TypeAlias = NameValuePair[IsocraticTemperatureName, float]

FlowPair = NameValuePair[FlowName, float]

IsocraticFlowPair: TypeAlias = NameValuePair[IsocraticFlowName, float]


# Unknowns for prototyping...

UnknownValue: TypeAlias = Value[str]

UNKNOWN_VALUE: Final[UnknownValue] = UnknownValue(value="TBD")


class UnknownPair(NameValuePair[_NameT, str]):
    pass


def unknown_pair(name: _NameT) -> UnknownPair[_NameT]:
    return UnknownPair(name=name, value="TBD")
