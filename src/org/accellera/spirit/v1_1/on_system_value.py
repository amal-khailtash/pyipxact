from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class OnSystemValue(Enum):
    IN = "in"
    OUT = "out"
    INOUT = "inout"