from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.complex_base_expression import (
    ComplexBaseExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class UnresolvedUnsignedBitExpression(ComplexBaseExpression):
    """
    Unsigned Bit Expression which cannot be fully resolved.
    """

    class Meta:
        name = "unresolvedUnsignedBitExpression"