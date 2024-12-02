from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


class ServiceTypeInitiative(Enum):
    REQUIRES = "requires"
    PROVIDES = "provides"
    BOTH = "both"
