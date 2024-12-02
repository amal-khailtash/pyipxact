from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


class FormatType(Enum):
    """This is an indication on the formatof the value for user defined properties.

    bitString means either a double quoted string of 1's an 0's or a
    scaledInteger number. bool means a boolean (true, false) is
    expected.  float means a decimal floating point number is expected.
    long means an value of scaledInteger is expected.  String means any
    text is acceptable.
    """

    BIT_STRING = "bitString"
    BOOL = "bool"
    FLOAT = "float"
    LONG = "long"
    STRING = "string"
