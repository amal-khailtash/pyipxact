from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


class EdgeValueType(Enum):
    """
    Indicates legal values for edge specification attributes.
    """

    RISE = "rise"
    FALL = "fall"
