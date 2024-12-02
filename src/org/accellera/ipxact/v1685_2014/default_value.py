from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class DefaultValue(UnsignedBitVectorExpression):
    """
    Default value for a wire port.
    """

    class Meta:
        name = "defaultValue"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
