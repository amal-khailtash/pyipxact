from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.addr_space_ref_type import (
    AddrSpaceRefType,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class AddressSpaceRef(AddrSpaceRefType):
    """References the address space.

    The name of the address space is kept in its addressSpaceRef
    attribute.
    """

    class Meta:
        name = "addressSpaceRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
