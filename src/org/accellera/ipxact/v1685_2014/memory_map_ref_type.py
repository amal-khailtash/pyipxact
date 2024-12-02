from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class MemoryMapRefType:
    """Base type for an element which references an memory map.

    Reference is kept in an attribute rather than the text value, so
    that the type may be extended with child elements if necessary.

    :ivar memory_map_ref: A reference to a unique memory map.
    """

    class Meta:
        name = "memoryMapRefType"

    memory_map_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "memoryMapRef",
            "type": "Attribute",
            "required": True,
        },
    )
