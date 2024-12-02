from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.unsigned_int_expression import (
    UnsignedIntExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Right(UnsignedIntExpression):
    """
    The optional element right specifies the right boundary.
    """

    class Meta:
        name = "right"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
