from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.unsigned_int_expression import (
    UnsignedIntExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class BusWidth(UnsignedIntExpression):
    """Defines the bus size in bits.

    This can be the result of an expression.
    """

    class Meta:
        name = "busWidth"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
