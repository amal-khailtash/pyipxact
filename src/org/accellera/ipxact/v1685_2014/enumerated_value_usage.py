from enum import Enum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


class EnumeratedValueUsage(Enum):
    READ = "read"
    WRITE = "write"
    READ_WRITE = "read-write"
