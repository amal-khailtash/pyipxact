from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


class DelayValueType(Enum):
    """Indicates the type of delay value - minimum or maximum delay."""

    MIN = "min"
    MAX = "max"
