from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class DirectionValue(Enum):
    """
    :cvar VERTICAL: Display radio buttons vertically
    :cvar HORIZONTAL: Display radio buttons horizontally (default)
    """

    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"
