from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.address_block_type import AddressBlockType
from org.accellera.ipxact.v1685_2022.banked_definition_bank_type import (
    BankedDefinitionBankType,
)
from org.accellera.ipxact.v1685_2022.description import Description
from org.accellera.ipxact.v1685_2022.display_name import DisplayName
from org.accellera.ipxact.v1685_2022.mode_ref import ModeRef
from org.accellera.ipxact.v1685_2022.short_description import ShortDescription
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class MemoryRemapDefinitionType:
    """
    Map of address space blocks on a target bus interface in a specific remap
    state.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar mode_ref:
    :ivar remap_definition_ref:
    :ivar address_block: An address block within the bank.  No address
        information is supplied.
    :ivar bank: A nested bank of blocks within a bank.  No address
        information is supplied.
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "memoryRemapDefinitionType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    mode_ref: Iterable[ModeRef] = field(
        default_factory=list,
        metadata={
            "name": "modeRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
        },
    )
    remap_definition_ref: Optional[
        "MemoryRemapDefinitionType.RemapDefinitionRef"
    ] = field(
        default=None,
        metadata={
            "name": "remapDefinitionRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    address_block: Iterable[AddressBlockType] = field(
        default_factory=list,
        metadata={
            "name": "addressBlock",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bank: Iterable["MemoryRemapDefinitionType.Bank"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass(slots=True)
    class RemapDefinitionRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_definitions: Optional[str] = field(
            default=None,
            metadata={
                "name": "typeDefinitions",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass(slots=True)
    class Bank(BankedDefinitionBankType):
        vendor_extensions: Optional[VendorExtensions] = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )