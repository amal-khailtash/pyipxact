from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class ComponentSignalDirectionType(Enum):
    """
    The direction of a component signal.
    """

    IN = "in"
    OUT = "out"
    INOUT = "inout"
