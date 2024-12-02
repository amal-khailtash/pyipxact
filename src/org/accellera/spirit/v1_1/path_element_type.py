from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class PathElementType(Enum):
    """
    Indicates legal values for pathElement attribute.
    """

    CLOCK = "clock"
    SIGNAL = "signal"
    PIN = "pin"
    CELL = "cell"
