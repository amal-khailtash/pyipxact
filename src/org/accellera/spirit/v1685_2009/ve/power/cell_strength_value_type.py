from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


class CellStrengthValueType(Enum):
    """
    Indicates legal cell strength values.
    """

    LOW = "low"
    MEDIAN = "median"
    HIGH = "high"
