from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class ReadResponse(UnsignedBitVectorExpression):
    class Meta:
        name = "readResponse"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
