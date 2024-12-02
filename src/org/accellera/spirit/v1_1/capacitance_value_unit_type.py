from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class CapacitanceValueUnitType(Enum):
    """
    Indicates legal units for capacitance values.
    """

    FF = "ff"
    PF = "pf"
