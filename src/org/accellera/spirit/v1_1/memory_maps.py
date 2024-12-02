from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.bits_in_lau import BitsInLau
from org.accellera.spirit.v1_1.memory_map_type import MemoryMapType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class MemoryMaps:
    """
    Lists all the slave memory maps defined by the component.

    :ivar memory_map: The set of address blocks a bus slave contributes
        to the bus' address space.
    """

    class Meta:
        name = "memoryMaps"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    memory_map: Iterable["MemoryMaps.MemoryMap"] = field(
        default_factory=list,
        metadata={
            "name": "memoryMap",
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class MemoryMap(MemoryMapType):
        bits_in_lau: Optional[BitsInLau] = field(
            default=None,
            metadata={
                "name": "bitsInLau",
                "type": "Element",
            },
        )
