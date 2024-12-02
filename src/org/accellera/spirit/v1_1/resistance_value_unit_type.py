from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class ResistanceValueUnitType(Enum):
    """
    Indicates legal units for resistance values.
    """

    OHM = "ohm"
    KOHM = "kohm"
