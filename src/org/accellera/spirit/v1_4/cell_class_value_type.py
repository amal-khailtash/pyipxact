from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


class CellClassValueType(Enum):
    """
    Indicates legal cell class values.
    """

    COMBINATIONAL = "combinational"
    SEQUENTIAL = "sequential"
