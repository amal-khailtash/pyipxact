from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class BitSteeringType(Enum):
    ON = "on"
    OFF = "off"
    DEFAULT = "default"