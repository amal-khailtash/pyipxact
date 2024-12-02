from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


class MonitorInterfaceMode(Enum):
    MASTER = "master"
    SLAVE = "slave"
    SYSTEM = "system"
    MIRRORED_MASTER = "mirroredMaster"
    MIRRORED_SLAVE = "mirroredSlave"
    MIRRORED_SYSTEM = "mirroredSystem"
