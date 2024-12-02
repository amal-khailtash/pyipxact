from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


class MonitorInterfaceMode(Enum):
    MASTER = "master"
    SLAVE = "slave"
    SYSTEM = "system"
    MIRRORED_MASTER = "mirroredMaster"
    MIRRORED_SLAVE = "mirroredSlave"
    MIRRORED_SYSTEM = "mirroredSystem"
