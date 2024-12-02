from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


class SimpleWhiteboxType(Enum):
    SIGNAL = "signal"
    PIN = "pin"
    INTERFACE = "interface"
