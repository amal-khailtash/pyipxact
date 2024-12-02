from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.unsigned_longint_expression import (
    UnsignedLongintExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class BaseAddress(UnsignedLongintExpression):
    """Base of an address block, bank, subspace map or address space.

    Expressed as the number of addressable units from the containing
    memoryMap or localMemoryMap.
    """

    class Meta:
        name = "baseAddress"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
