from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


class ResistanceValueUnitType(Enum):
    """
    Indicates legal units for resistance values.
    """

    OHM = "ohm"
    KOHM = "kohm"
