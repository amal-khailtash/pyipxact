from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class AddrSpaceRefType:
    """Base type for an element which references an address space.

    Reference is kept in an attribute rather than the text value, so
    that the type may be extended with child elements if necessary.
    """

    class Meta:
        name = "addrSpaceRefType"

    address_space_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "addressSpaceRef",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            "required": True,
        },
    )
