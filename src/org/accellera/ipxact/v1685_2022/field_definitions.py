from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.access import Access
from org.accellera.ipxact.v1685_2022.access_restrictions import (
    AccessRestrictions,
)
from org.accellera.ipxact.v1685_2022.address_block_ref import AddressBlockRef
from org.accellera.ipxact.v1685_2022.alternate_register_ref import (
    AlternateRegisterRef,
)
from org.accellera.ipxact.v1685_2022.bank_ref import BankRef
from org.accellera.ipxact.v1685_2022.description import Description
from org.accellera.ipxact.v1685_2022.display_name import DisplayName
from org.accellera.ipxact.v1685_2022.enumerated_values import EnumeratedValues
from org.accellera.ipxact.v1685_2022.field_access_policy_definition_ref import (
    FieldAccessPolicyDefinitionRef,
)
from org.accellera.ipxact.v1685_2022.field_access_properties_type import (
    FieldAccessPropertiesType,
)
from org.accellera.ipxact.v1685_2022.field_ref import FieldRef
from org.accellera.ipxact.v1685_2022.memory_remap_ref import MemoryRemapRef
from org.accellera.ipxact.v1685_2022.mode_ref import ModeRef
from org.accellera.ipxact.v1685_2022.modified_write_value import (
    ModifiedWriteValue,
)
from org.accellera.ipxact.v1685_2022.read_action import ReadAction
from org.accellera.ipxact.v1685_2022.read_response import ReadResponse
from org.accellera.ipxact.v1685_2022.register_file_ref import RegisterFileRef
from org.accellera.ipxact.v1685_2022.register_ref import RegisterRef
from org.accellera.ipxact.v1685_2022.reset import Reset
from org.accellera.ipxact.v1685_2022.short_description import ShortDescription
from org.accellera.ipxact.v1685_2022.testable_test_constraint import (
    TestableTestConstraint,
)
from org.accellera.ipxact.v1685_2022.unsigned_bit_expression import (
    UnsignedBitExpression,
)
from org.accellera.ipxact.v1685_2022.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions
from org.accellera.ipxact.v1685_2022.write_value_constraint import (
    WriteValueConstraint,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class FieldDefinitions:
    class Meta:
        name = "fieldDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    field_definition: Iterable["FieldDefinitions.FieldDefinition"] = field(
        default_factory=list,
        metadata={
            "name": "fieldDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class FieldDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar type_identifier: Identifier name used to indicate that
            multiple field elements contain the exact same information
            for the elements in the fieldDefinitionGroup.
        :ivar bit_width: Width of the field in bits.
        :ivar volatile: Indicates whether the data is volatile. The
            presumed value is 'false' if not present.
        :ivar resets:
        :ivar field_access_policies:
        :ivar enumerated_values:
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
        bit_width: Optional[UnsignedPositiveIntExpression] = field(
            default=None,
            metadata={
                "name": "bitWidth",
                "type": "Element",
                "required": True,
            },
        )
        volatile: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        resets: Optional["FieldDefinitions.FieldDefinition.Resets"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        field_access_policies: Optional[
            "FieldDefinitions.FieldDefinition.FieldAccessPolicies"
        ] = field(
            default=None,
            metadata={
                "name": "fieldAccessPolicies",
                "type": "Element",
            },
        )
        enumerated_values: Optional[EnumeratedValues] = field(
            default=None,
            metadata={
                "name": "enumeratedValues",
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
        class Resets:
            """
            :ivar reset: BitField reset value
            """

            reset: Iterable[Reset] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

        @dataclass(slots=True)
        class FieldAccessPolicies(FieldAccessPropertiesType):
            field_access_policy: Iterable[
                "FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "fieldAccessPolicy",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(slots=True)
            class FieldAccessPolicy:
                """
                :ivar mode_ref:
                :ivar field_access_policy_definition_ref:
                :ivar access:
                :ivar modified_write_value:
                :ivar write_value_constraint:
                :ivar read_action:
                :ivar read_response:
                :ivar broadcasts:
                :ivar access_restrictions: Access restrictions
                :ivar testable: Can the field be tested with an
                    automated register test routine. The presumed value
                    is true if not specified.
                :ivar reserved: Indicates that the field should be
                    documented as reserved. The presumed value is '0' if
                    not present.
                :ivar vendor_extensions:
                :ivar id:
                """

                mode_ref: Iterable[ModeRef] = field(
                    default_factory=list,
                    metadata={
                        "name": "modeRef",
                        "type": "Element",
                    },
                )
                field_access_policy_definition_ref: Optional[
                    FieldAccessPolicyDefinitionRef
                ] = field(
                    default=None,
                    metadata={
                        "name": "fieldAccessPolicyDefinitionRef",
                        "type": "Element",
                    },
                )
                access: Optional[Access] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                modified_write_value: Optional[ModifiedWriteValue] = field(
                    default=None,
                    metadata={
                        "name": "modifiedWriteValue",
                        "type": "Element",
                    },
                )
                write_value_constraint: Optional[WriteValueConstraint] = field(
                    default=None,
                    metadata={
                        "name": "writeValueConstraint",
                        "type": "Element",
                    },
                )
                read_action: Optional[ReadAction] = field(
                    default=None,
                    metadata={
                        "name": "readAction",
                        "type": "Element",
                    },
                )
                read_response: Optional[ReadResponse] = field(
                    default=None,
                    metadata={
                        "name": "readResponse",
                        "type": "Element",
                    },
                )
                broadcasts: Optional[
                    "FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy.Broadcasts"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                access_restrictions: Optional[AccessRestrictions] = field(
                    default=None,
                    metadata={
                        "name": "accessRestrictions",
                        "type": "Element",
                    },
                )
                testable: Optional[
                    "FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy.Testable"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                reserved: Optional[UnsignedBitExpression] = field(
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
                class Broadcasts:
                    broadcast_to: Iterable[
                        "FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy.Broadcasts.BroadcastTo"
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "broadcastTo",
                            "type": "Element",
                            "min_occurs": 1,
                        },
                    )

                    @dataclass(slots=True)
                    class BroadcastTo:
                        address_space_ref: Optional[
                            "FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy.Broadcasts.BroadcastTo.AddressSpaceRef"
                        ] = field(
                            default=None,
                            metadata={
                                "name": "addressSpaceRef",
                                "type": "Element",
                            },
                        )
                        memory_map_ref: Optional[
                            "FieldDefinitions.FieldDefinition.FieldAccessPolicies.FieldAccessPolicy.Broadcasts.BroadcastTo.MemoryMapRef"
                        ] = field(
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
                        alternate_register_ref: Optional[
                            AlternateRegisterRef
                        ] = field(
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
                        id: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Attribute",
                                "namespace": "http://www.w3.org/XML/1998/namespace",
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

                @dataclass(slots=True)
                class Testable:
                    """
                    :ivar value:
                    :ivar test_constraint: Constraint for an automated
                        register test routine. 'unconstrained' (default)
                        means may read and write all legal values.
                        'restore' means may read and write legal values
                        but the value must be restored to the initially
                        read value before accessing another register.
                        'writeAsRead' has limitations on testability
                        where only the value read before a write may be
                        written to the field. 'readOnly' has limitations
                        on testability where values may only be read
                        from the field.
                    """

                    value: Optional[bool] = field(
                        default=None,
                        metadata={
                            "required": True,
                        },
                    )
                    test_constraint: TestableTestConstraint = field(
                        default=TestableTestConstraint.UNCONSTRAINED,
                        metadata={
                            "name": "testConstraint",
                            "type": "Attribute",
                        },
                    )
