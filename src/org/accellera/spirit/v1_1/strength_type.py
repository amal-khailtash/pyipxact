from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class StrengthType(Enum):
    """
    Describes a signal strength.
    """

    STRONG = "strong"
    WEAK = "weak"
