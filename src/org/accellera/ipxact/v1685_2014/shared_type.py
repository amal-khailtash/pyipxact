from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


class SharedType(Enum):
    """
    The sharedness of the memoryMap content.
    """

    YES = "yes"
    NO = "no"
    UNDEFINED = "undefined"
