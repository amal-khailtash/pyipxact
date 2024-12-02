from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class BitStride(UnsignedPositiveLongintExpression):
    class Meta:
        name = "bitStride"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
