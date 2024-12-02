from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class RelativeClockType(Enum):
    """
    Indicates legal values for associating a clock with timing exception.
    """

    START = "start"
    END = "end"
