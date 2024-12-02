from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


class FieldTypeReadAction(Enum):
    CLEAR = "clear"
    SET = "set"
    MODIFY = "modify"
