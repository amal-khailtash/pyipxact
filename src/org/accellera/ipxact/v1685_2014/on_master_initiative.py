from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


class OnMasterInitiative(Enum):
    REQUIRES = "requires"
    PROVIDES = "provides"
    BOTH = "both"