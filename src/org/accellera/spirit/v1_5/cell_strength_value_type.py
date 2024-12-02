from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


class CellStrengthValueType(Enum):
    """
    Indicates legal cell strength values.
    """

    LOW = "low"
    MEDIAN = "median"
    HIGH = "high"
