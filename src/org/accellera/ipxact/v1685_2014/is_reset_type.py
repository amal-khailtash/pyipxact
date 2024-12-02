from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.unsigned_bit_expression import (
    UnsignedBitExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class IsResetType(UnsignedBitExpression):
    """If this evaluates to true, it indicates this port triggers the reset of
    registers and fields, if not present its value is assumed to be false.

    The resetTypeRef attribute indicates the triggered reset event.

    :ivar reset_type_ref: Reference to a user defined resetType. Assumed
        to be HARD if not present.
    :ivar id:
    """

    class Meta:
        name = "isResetType"

    reset_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "resetTypeRef",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
