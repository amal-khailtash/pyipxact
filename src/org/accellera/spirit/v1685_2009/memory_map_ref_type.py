from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class MemoryMapRefType:
    """Base type for an element which references an memory map.

    Reference is kept in an attribute rather than the text value, so
    that the type may be extended with child elements if necessary.
    """

    class Meta:
        name = "memoryMapRefType"

    memory_map_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "memoryMapRef",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "required": True,
        },
    )
