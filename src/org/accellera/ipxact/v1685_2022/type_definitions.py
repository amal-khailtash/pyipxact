from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.address_block_definitions import (
    AddressBlockDefinitions,
)
from org.accellera.ipxact.v1685_2022.assertions import Assertions
from org.accellera.ipxact.v1685_2022.bank_definitions import BankDefinitions
from org.accellera.ipxact.v1685_2022.choices import Choices
from org.accellera.ipxact.v1685_2022.description import Description
from org.accellera.ipxact.v1685_2022.display_name import DisplayName
from org.accellera.ipxact.v1685_2022.enumeration_definitions import (
    EnumerationDefinitions,
)
from org.accellera.ipxact.v1685_2022.external_type_definitions import (
    ExternalTypeDefinitions,
)
from org.accellera.ipxact.v1685_2022.field_access_policy_definitions import (
    FieldAccessPolicyDefinitions,
)
from org.accellera.ipxact.v1685_2022.field_definitions import FieldDefinitions
from org.accellera.ipxact.v1685_2022.memory_map_definitions import (
    MemoryMapDefinitions,
)
from org.accellera.ipxact.v1685_2022.memory_remap_definitions import (
    MemoryRemapDefinitions,
)
from org.accellera.ipxact.v1685_2022.parameters import Parameters
from org.accellera.ipxact.v1685_2022.register_definitions import (
    RegisterDefinitions,
)
from org.accellera.ipxact.v1685_2022.register_file_definitions import (
    RegisterFileDefinitions,
)
from org.accellera.ipxact.v1685_2022.short_description import ShortDescription
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class TypeDefinitions:
    """
    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar display_name: Name for display purposes. Typically a few words
        providing a more detailed and/or user-friendly name than the
        vlnv.
    :ivar short_description:
    :ivar description:
    :ivar external_type_definitions:
    :ivar modes: A list of user defined component modes.
    :ivar views: A list of user defined views.
    :ivar field_access_policy_definitions:
    :ivar enumeration_definitions:
    :ivar field_definitions:
    :ivar register_definitions:
    :ivar register_file_definitions:
    :ivar address_block_definitions:
    :ivar bank_definitions:
    :ivar memory_map_definitions:
    :ivar memory_remap_definitions:
    :ivar reset_types: A list of user defined resetTypes applicable to
        this component.
    :ivar choices:
    :ivar parameters:
    :ivar assertions:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "typeDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    display_name: Optional[str] = field(
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
    external_type_definitions: Iterable[ExternalTypeDefinitions] = field(
        default_factory=list,
        metadata={
            "name": "externalTypeDefinitions",
            "type": "Element",
        },
    )
    modes: Optional["TypeDefinitions.Modes"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    views: Optional["TypeDefinitions.Views"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    field_access_policy_definitions: Optional[FieldAccessPolicyDefinitions] = (
        field(
            default=None,
            metadata={
                "name": "fieldAccessPolicyDefinitions",
                "type": "Element",
            },
        )
    )
    enumeration_definitions: Optional[EnumerationDefinitions] = field(
        default=None,
        metadata={
            "name": "enumerationDefinitions",
            "type": "Element",
        },
    )
    field_definitions: Optional[FieldDefinitions] = field(
        default=None,
        metadata={
            "name": "fieldDefinitions",
            "type": "Element",
        },
    )
    register_definitions: Optional[RegisterDefinitions] = field(
        default=None,
        metadata={
            "name": "registerDefinitions",
            "type": "Element",
        },
    )
    register_file_definitions: Optional[RegisterFileDefinitions] = field(
        default=None,
        metadata={
            "name": "registerFileDefinitions",
            "type": "Element",
        },
    )
    address_block_definitions: Optional[AddressBlockDefinitions] = field(
        default=None,
        metadata={
            "name": "addressBlockDefinitions",
            "type": "Element",
        },
    )
    bank_definitions: Optional[BankDefinitions] = field(
        default=None,
        metadata={
            "name": "bankDefinitions",
            "type": "Element",
        },
    )
    memory_map_definitions: Optional[MemoryMapDefinitions] = field(
        default=None,
        metadata={
            "name": "memoryMapDefinitions",
            "type": "Element",
        },
    )
    memory_remap_definitions: Optional[MemoryRemapDefinitions] = field(
        default=None,
        metadata={
            "name": "memoryRemapDefinitions",
            "type": "Element",
        },
    )
    reset_types: Optional["TypeDefinitions.ResetTypes"] = field(
        default=None,
        metadata={
            "name": "resetTypes",
            "type": "Element",
        },
    )
    choices: Optional[Choices] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    assertions: Optional[Assertions] = field(
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
    class Modes:
        mode: Iterable["TypeDefinitions.Modes.Mode"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(slots=True)
        class Mode:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
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
    class Views:
        view: Iterable["TypeDefinitions.Views.View"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(slots=True)
        class View:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
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
    class ResetTypes:
        """
        :ivar reset_type: A user defined reset policy
        """

        reset_type: Iterable["TypeDefinitions.ResetTypes.ResetType"] = field(
            default_factory=list,
            metadata={
                "name": "resetType",
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(slots=True)
        class ResetType:
            """
            :ivar name: Unique name
            :ivar display_name:
            :ivar short_description:
            :ivar description:
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
