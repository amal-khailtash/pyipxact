from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


class DelayValueUnitType(Enum):
    """
    Indicates legal units for delay values.
    """

    PS = "ps"
    NS = "ns"
