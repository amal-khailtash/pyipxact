from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


class AbstractorModeType(Enum):
    """
    Mode for this abstractor.
    """

    MASTER = "master"
    SLAVE = "slave"
    DIRECT = "direct"
    SYSTEM = "system"
