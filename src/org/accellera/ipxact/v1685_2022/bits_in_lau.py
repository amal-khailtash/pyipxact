from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class BitsInLau(UnsignedPositiveLongintExpression):
    """The number of bits in the least addressable unit.

    The default is byte addressable (8 bits).
    """

    class Meta:
        name = "bitsInLau"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
