from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


class ChoiceStyleValue(Enum):
    """
    :cvar RADIO: Display choice as radio buttons (default).
    :cvar COMBO: Display choice as combo box.
    """

    RADIO = "radio"
    COMBO = "combo"
