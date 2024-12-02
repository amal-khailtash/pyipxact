from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


class InitiativeValue(Enum):
    REQUIRES = "requires"
    PROVIDES = "provides"
    BOTH = "both"
    PHANTOM = "phantom"
