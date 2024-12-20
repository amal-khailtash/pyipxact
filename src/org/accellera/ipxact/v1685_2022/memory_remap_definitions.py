from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.address_bank_definition_type import (
    AddressBankDefinitionType,
)
from org.accellera.ipxact.v1685_2022.address_block import AddressBlock
from org.accellera.ipxact.v1685_2022.address_unit_bits import AddressUnitBits
from org.accellera.ipxact.v1685_2022.description import Description
from org.accellera.ipxact.v1685_2022.display_name import DisplayName
from org.accellera.ipxact.v1685_2022.short_description import ShortDescription
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class MemoryRemapDefinitions:
    class Meta:
        name = "memoryRemapDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    memory_remap_definition: Iterable[
        "MemoryRemapDefinitions.MemoryRemapDefinition"
    ] = field(
        default_factory=list,
        metadata={
            "name": "memoryRemapDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class MemoryRemapDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar address_block:
        :ivar bank: An addressable bank of blocks within a bank
            definition.
        :ivar address_unit_bits:
        :ivar vendor_extensions:
        :ivar id:
        """

        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        display_name: Optional[DisplayName] = field(
            default=None,
            metadata={
                "name": "displayName",
                "type": "Element",
            },
        )
        short_description: Optional[ShortDescription] = field(
            default=None,
            metadata={
                "name": "shortDescription",
                "type": "Element",
            },
        )
        description: Optional[Description] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        address_block: Iterable[AddressBlock] = field(
            default_factory=list,
            metadata={
                "name": "addressBlock",
                "type": "Element",
            },
        )
        bank: Iterable[AddressBankDefinitionType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        address_unit_bits: Optional[AddressUnitBits] = field(
            default=None,
            metadata={
                "name": "addressUnitBits",
                "type": "Element",
            },
        )
        vendor_extensions: Optional[VendorExtensions] = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
