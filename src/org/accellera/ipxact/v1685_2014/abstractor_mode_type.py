from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


class AbstractorModeType(Enum):
    """
    Mode for this abstractor.
    """

    MASTER = "master"
    SLAVE = "slave"
    DIRECT = "direct"
    SYSTEM = "system"
