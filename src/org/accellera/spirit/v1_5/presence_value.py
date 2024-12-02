from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


class PresenceValue(Enum):
    REQUIRED = "required"
    ILLEGAL = "illegal"
    OPTIONAL = "optional"
