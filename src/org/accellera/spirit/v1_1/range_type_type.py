from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


class RangeTypeType(Enum):
    """This type is used to indicate how the minimum and maximum attributes values
    should be interpreted.

    For purposes of this attribute, an int is 4 bytes and a long is 8
    bytes.
    """

    FLOAT = "float"
    INT = "int"
    UNSIGNED_INT = "unsigned int"
    LONG = "long"
    UNSIGNED_LONG = "unsigned long"
