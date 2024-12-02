from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2014.memory_map_type import MemoryMapType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class MemoryMaps:
    """
    Lists all the slave memory maps defined by the component.

    :ivar memory_map: The set of address blocks a bus slave contributes
        to the bus' address space.
    """

    class Meta:
        name = "memoryMaps"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    memory_map: Iterable[MemoryMapType] = field(
        default_factory=list,
        metadata={
            "name": "memoryMap",
            "type": "Element",
            "min_occurs": 1,
        },
    )
