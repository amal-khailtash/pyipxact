from dataclasses import dataclass

from org.accellera.spirit.v1_1.addr_space_ref_type import AddrSpaceRefType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class AddressSpaceRef(AddrSpaceRefType):
    """References the address space.

    The name of the address space is kept in its addressSpaceRef
    attribute.
    """

    class Meta:
        name = "addressSpaceRef"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"
