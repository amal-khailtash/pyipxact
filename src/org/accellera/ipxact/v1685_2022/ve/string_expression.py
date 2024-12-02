from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.ve.complex_base_expression import (
    ComplexBaseExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class StringExpression(ComplexBaseExpression):
    """Represents a string.

    It supports an expression value.
    """

    class Meta:
        name = "stringExpression"
