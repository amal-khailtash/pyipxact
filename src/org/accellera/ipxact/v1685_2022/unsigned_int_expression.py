from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.complex_base_expression import (
    ComplexBaseExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class UnsignedIntExpression(ComplexBaseExpression):
    """
    An unsigned int which supports an expression value.

    :ivar minimum: For elements which can be specified using expression
        which are supposed to be resolved to an unsiged int value, this
        indicates the minimum value allowed.
    :ivar maximum: For elements which can be specified using expression
        which are supposed to be resolved to a unsigned int value, this
        indicates the maximum value allowed.
    """

    class Meta:
        name = "unsignedIntExpression"

    minimum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maximum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )