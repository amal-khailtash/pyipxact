from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


class InstanceGeneratorTypeScope(Enum):
    INSTANCE = "instance"
    ENTITY = "entity"