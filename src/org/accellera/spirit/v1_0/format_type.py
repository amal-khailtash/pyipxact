from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


class FormatType(Enum):
    """This is a hint to the user interface on how to obtain the value for user
    defined properties.

    Float means a floating point number is expected.  Long means an
    integer is expected.  Bool means a boolean (true, false) is expected
    and choice means the user must pick from a list of possible values.
    A choiceRef attribute is required for choice formats.  String means
    any text is acceptable.
    """

    FLOAT = "float"
    LONG = "long"
    BOOL = "bool"
    CHOICE = "choice"
    STRING = "string"
