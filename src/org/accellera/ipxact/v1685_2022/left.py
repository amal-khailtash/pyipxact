from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.unsigned_int_expression import (
    UnsignedIntExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Left(UnsignedIntExpression):
    """
    The optional element left specifies the left boundary.
    """

    class Meta:
        name = "left"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
