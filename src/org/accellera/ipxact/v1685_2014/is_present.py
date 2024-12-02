from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.unsigned_bit_expression import (
    UnsignedBitExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class IsPresent(UnsignedBitExpression):
    """
    Expression that determines whether the enclosing element should be treated as
    present (expression evaluates to "true") or disregarded (expression evalutes to
    "false")
    """

    class Meta:
        name = "isPresent"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
