from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1685_2009.ve.power.memory_map_type import (
    MemoryMapType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class MemoryMaps:
    """
    Lists all the slave memory maps defined by the component.

    :ivar memory_map: The set of address blocks a bus slave contributes
        to the bus' address space.
    """

    class Meta:
        name = "memoryMaps"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    memory_map: Iterable[MemoryMapType] = field(
        default_factory=list,
        metadata={
            "name": "memoryMap",
            "type": "Element",
            "min_occurs": 1,
        },
    )
