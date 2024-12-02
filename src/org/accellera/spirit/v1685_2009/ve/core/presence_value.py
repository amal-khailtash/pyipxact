from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


class PresenceValue(Enum):
    REQUIRED = "required"
    ILLEGAL = "illegal"
    OPTIONAL = "optional"
