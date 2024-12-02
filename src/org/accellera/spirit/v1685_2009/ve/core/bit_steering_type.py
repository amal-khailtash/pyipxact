from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


class BitSteeringType(Enum):
    """Indicates whether bit steering should be used to map this interface onto a
    bus of different data width.

    Values are "on", "off" (defaults to "off").
    """

    ON = "on"
    OFF = "off"
