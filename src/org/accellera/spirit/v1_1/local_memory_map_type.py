from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_1.address_block import AddressBlock
from org.accellera.spirit.v1_1.bank import Bank
from org.accellera.spirit.v1_1.subspace_ref_type import SubspaceRefType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class LocalMemoryMapType:
    """
    Map of address space blocks on the local memory map of a master bus interface.

    :ivar address_block:
    :ivar bank:
    :ivar subspace_map: Maps in an address subspace from accross a bus
        bridge.  Its masterRef attribute refers by name to the master
        bus interface on the other side of the bridge.  It must match
        the masterRef attribute of a bridge element on the slave
        interface, and that bridge element must be designated as opaque.
    """

    class Meta:
        name = "localMemoryMapType"

    address_block: Iterable[AddressBlock] = field(
        default_factory=list,
        metadata={
            "name": "addressBlock",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    bank: Iterable[Bank] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    subspace_map: Iterable[SubspaceRefType] = field(
        default_factory=list,
        metadata={
            "name": "subspaceMap",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
