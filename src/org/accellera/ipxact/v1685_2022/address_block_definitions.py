from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.access_policies import AccessPolicies
from org.accellera.ipxact.v1685_2022.address_unit_bits import AddressUnitBits
from org.accellera.ipxact.v1685_2022.alternate_registers import (
    AlternateRegisters,
)
from org.accellera.ipxact.v1685_2022.array import Array
from org.accellera.ipxact.v1685_2022.description import Description
from org.accellera.ipxact.v1685_2022.display_name import DisplayName
from org.accellera.ipxact.v1685_2022.field_type import FieldType
from org.accellera.ipxact.v1685_2022.parameters import Parameters
from org.accellera.ipxact.v1685_2022.register_file import RegisterFile
from org.accellera.ipxact.v1685_2022.short_description import ShortDescription
from org.accellera.ipxact.v1685_2022.simple_access_handle import (
    SimpleAccessHandle,
)
from org.accellera.ipxact.v1685_2022.unsigned_longint_expression import (
    UnsignedLongintExpression,
)
from org.accellera.ipxact.v1685_2022.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from org.accellera.ipxact.v1685_2022.unsigned_positive_longint_expression import (
    UnsignedPositiveLongintExpression,
)
from org.accellera.ipxact.v1685_2022.usage_type import UsageType
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions
from org.accellera.ipxact.v1685_2022.volatile import Volatile

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class AddressBlockDefinitions:
    class Meta:
        name = "addressBlockDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    address_block_definition: Iterable[
        "AddressBlockDefinitions.AddressBlockDefinition"
    ] = field(
        default_factory=list,
        metadata={
            "name": "addressBlockDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class AddressBlockDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar type_identifier: Identifier name used to indicate that
            multiple addressBlock elements contain the exact same
            information except for the elements in the
            addressBlockInstanceGroup.
        :ivar range: The address range of an address block.  Expressed
            as the number of addressable units accessible to the block.
            The range and the width are related by the following
            formulas: number_of_bits_in_block = ipxact:addressUnitBits *
            ipxact:range number_of_rows_in_block =
            number_of_bits_in_block / ipxact:width
        :ivar width: The bit width of a row in the address block. The
            range and the width are related by the following formulas:
            number_of_bits_in_block = ipxact:addressUnitBits *
            ipxact:range number_of_rows_in_block =
            number_of_bits_in_block / ipxact:width
        :ivar usage: Indicates the usage of this block.  Possible values
            are 'memory', 'register' and 'reserved'.
        :ivar volatile:
        :ivar access_policies:
        :ivar parameters: Any additional parameters needed to describe
            this address block to the generators.
        :ivar register: A single register
        :ivar register_file: A structure of registers and register files
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
        type_identifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "typeIdentifier",
                "type": "Element",
            },
        )
        range: Optional[UnsignedPositiveLongintExpression] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        width: Optional[UnsignedPositiveIntExpression] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        usage: Optional[UsageType] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        volatile: Optional[Volatile] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        access_policies: Optional[AccessPolicies] = field(
            default=None,
            metadata={
                "name": "accessPolicies",
                "type": "Element",
            },
        )
        parameters: Optional[Parameters] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        register: Iterable[
            "AddressBlockDefinitions.AddressBlockDefinition.Register"
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        register_file: Iterable[RegisterFile] = field(
            default_factory=list,
            metadata={
                "name": "registerFile",
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

        @dataclass(slots=True)
        class Register:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
            :ivar access_handles:
            :ivar array:
            :ivar address_offset: Offset from the address block's
                baseAddress or the containing register file's
                addressOffset, expressed as the number of
                addressUnitBits from the containing memoryMap or
                localMemoryMap.
            :ivar register_definition_ref:
            :ivar type_identifier: Identifier name used to indicate that
                multiple register elements contain the exact same
                information for the elements in the
                registerDefinitionGroup.
            :ivar size: Width of the register in bits.
            :ivar volatile:
            :ivar access_policies:
            :ivar field_value: Describes individual bit fields within
                the register.
            :ivar alternate_registers:
            :ivar parameters:
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
            access_handles: Optional[
                "AddressBlockDefinitions.AddressBlockDefinition.Register.AccessHandles"
            ] = field(
                default=None,
                metadata={
                    "name": "accessHandles",
                    "type": "Element",
                },
            )
            array: Optional[Array] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            address_offset: Optional[UnsignedLongintExpression] = field(
                default=None,
                metadata={
                    "name": "addressOffset",
                    "type": "Element",
                    "required": True,
                },
            )
            register_definition_ref: Optional[
                "AddressBlockDefinitions.AddressBlockDefinition.Register.RegisterDefinitionRef"
            ] = field(
                default=None,
                metadata={
                    "name": "registerDefinitionRef",
                    "type": "Element",
                },
            )
            type_identifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "typeIdentifier",
                    "type": "Element",
                },
            )
            size: Optional[UnsignedPositiveIntExpression] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            volatile: Optional[Volatile] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            access_policies: Optional[AccessPolicies] = field(
                default=None,
                metadata={
                    "name": "accessPolicies",
                    "type": "Element",
                },
            )
            field_value: Iterable[FieldType] = field(
                default_factory=list,
                metadata={
                    "name": "field",
                    "type": "Element",
                },
            )
            alternate_registers: Optional[AlternateRegisters] = field(
                default=None,
                metadata={
                    "name": "alternateRegisters",
                    "type": "Element",
                },
            )
            parameters: Optional[Parameters] = field(
                default=None,
                metadata={
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

            @dataclass(slots=True)
            class AccessHandles:
                access_handle: Iterable[SimpleAccessHandle] = field(
                    default_factory=list,
                    metadata={
                        "name": "accessHandle",
                        "type": "Element",
                        "min_occurs": 1,
                    },
                )

            @dataclass(slots=True)
            class RegisterDefinitionRef:
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
