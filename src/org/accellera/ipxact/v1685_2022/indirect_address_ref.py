from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.address_block_ref import AddressBlockRef
from org.accellera.ipxact.v1685_2022.alternate_register_ref import (
    AlternateRegisterRef,
)
from org.accellera.ipxact.v1685_2022.bank_ref import BankRef
from org.accellera.ipxact.v1685_2022.field_ref import FieldRef
from org.accellera.ipxact.v1685_2022.memory_remap_ref import MemoryRemapRef
from org.accellera.ipxact.v1685_2022.register_file_ref import RegisterFileRef
from org.accellera.ipxact.v1685_2022.register_ref import RegisterRef

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class IndirectAddressRef:
    """
    A reference to a field used for addressing the indirectly accessible memoryMap.
    """

    class Meta:
        name = "indirectAddressRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    address_space_ref: Optional["IndirectAddressRef.AddressSpaceRef"] = field(
        default=None,
        metadata={
            "name": "addressSpaceRef",
            "type": "Element",
        },
    )
    memory_map_ref: Optional["IndirectAddressRef.MemoryMapRef"] = field(
        default=None,
        metadata={
            "name": "memoryMapRef",
            "type": "Element",
        },
    )
    memory_remap_ref: Optional[MemoryRemapRef] = field(
        default=None,
        metadata={
            "name": "memoryRemapRef",
            "type": "Element",
        },
    )
    bank_ref: Iterable[BankRef] = field(
        default_factory=list,
        metadata={
            "name": "bankRef",
            "type": "Element",
        },
    )
    address_block_ref: Optional[AddressBlockRef] = field(
        default=None,
        metadata={
            "name": "addressBlockRef",
            "type": "Element",
        },
    )
    register_file_ref: Iterable[RegisterFileRef] = field(
        default_factory=list,
        metadata={
            "name": "registerFileRef",
            "type": "Element",
        },
    )
    register_ref: Optional[RegisterRef] = field(
        default=None,
        metadata={
            "name": "registerRef",
            "type": "Element",
        },
    )
    alternate_register_ref: Optional[AlternateRegisterRef] = field(
        default=None,
        metadata={
            "name": "alternateRegisterRef",
            "type": "Element",
        },
    )
    field_ref: Optional[FieldRef] = field(
        default=None,
        metadata={
            "name": "fieldRef",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass(slots=True)
    class AddressSpaceRef:
        address_space_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "addressSpaceRef",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass(slots=True)
    class MemoryMapRef:
        memory_map_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "memoryMapRef",
                "type": "Attribute",
                "required": True,
            },
        )
