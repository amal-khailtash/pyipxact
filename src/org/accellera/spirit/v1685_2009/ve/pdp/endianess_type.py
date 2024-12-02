from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


class EndianessType(Enum):
    """'big': means the most significant element of any multi-element  data field
    is stored at the lowest memory address.

    'little' means the least significant element of any multi-element
    data field is stored at the lowest memory address. If this element
    is not present the default is 'little' endian.
    """

    BIG = "big"
    LITTLE = "little"
