from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


class WhiteboxElementTypeWhiteboxType(Enum):
    REGISTER = "register"
    SIGNAL = "signal"
    PIN = "pin"
    INTERFACE = "interface"