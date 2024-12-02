from enum import Enum

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0"
)


class TypeValue(Enum):
    ASIC = "ASIC"
    FPGA = "FPGA"
