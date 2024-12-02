from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.memory_map_ref_type import (
    MemoryMapRefType,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class MemoryMapRef(MemoryMapRefType):
    """References the memory map.

    The name of the memory map is kept in its memoryMapRef attribute.
    """

    class Meta:
        name = "memoryMapRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
