from enum import Enum

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


class EnumeratedValueUsage(Enum):
    READ = "read"
    WRITE = "write"
    READ_WRITE = "read-write"
