from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


class OnSlaveDirection(Enum):
    IN = "in"
    OUT = "out"
    INOUT = "inout"
