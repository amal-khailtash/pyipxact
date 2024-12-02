from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class CheckValueType(Enum):
    """Indicates legal values for type of checking the paths apply to: setup or hold."""

    SETUP = "setup"
    HOLD = "hold"
