from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


class DelayValueType(Enum):
    """Indicates the type of delay value - minimum or maximum delay."""

    MIN = "min"
    MAX = "max"