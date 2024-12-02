from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.unsigned_bit_expression import (
    UnsignedBitExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class AlwaysOn(UnsignedBitExpression):
    """Boolean value.

    If set to true, then the domain/port is always powered, whatever its
    power domain. Only applies for output ports.
    """

    class Meta:
        name = "alwaysOn"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
