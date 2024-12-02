from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


class ComponentPortDirectionType(Enum):
    """
    The direction of a component port.
    """

    IN = "in"
    OUT = "out"
    INOUT = "inout"
    PHANTOM = "phantom"
