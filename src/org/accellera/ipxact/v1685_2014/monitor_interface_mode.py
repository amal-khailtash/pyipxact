from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


class MonitorInterfaceMode(Enum):
    MASTER = "master"
    SLAVE = "slave"
    SYSTEM = "system"
    MIRRORED_MASTER = "mirroredMaster"
    MIRRORED_SLAVE = "mirroredSlave"
    MIRRORED_SYSTEM = "mirroredSystem"
