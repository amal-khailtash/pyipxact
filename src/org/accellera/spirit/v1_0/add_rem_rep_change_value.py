from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


class AddRemRepChangeValue(Enum):
    ADD = "add"
    REMOVE = "remove"
    REPLACE = "replace"
