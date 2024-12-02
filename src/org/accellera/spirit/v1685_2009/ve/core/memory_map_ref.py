from dataclasses import dataclass

from org.accellera.spirit.v1685_2009.ve.core.memory_map_ref_type import (
    MemoryMapRefType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class MemoryMapRef(MemoryMapRefType):
    """References the memory map.

    The name of the memory map is kept in its memoryMapRef attribute.
    """

    class Meta:
        name = "memoryMapRef"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )
