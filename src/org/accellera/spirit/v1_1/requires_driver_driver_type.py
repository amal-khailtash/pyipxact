from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class RequiresDriverDriverType(Enum):
    CLOCK = "clock"
    SINGLE_SHOT = "singleShot"
    ANY = "any"
