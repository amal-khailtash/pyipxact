from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.access import Access
from org.accellera.ipxact.v1685_2014.description import Description
from org.accellera.ipxact.v1685_2014.display_name import DisplayName
from org.accellera.ipxact.v1685_2014.field_type import FieldType
from org.accellera.ipxact.v1685_2014.indexed_access_handle import (
    IndexedAccessHandle,
)
from org.accellera.ipxact.v1685_2014.is_present import IsPresent
from org.accellera.ipxact.v1685_2014.parameters import Parameters
from org.accellera.ipxact.v1685_2014.vendor_extensions import VendorExtensions
from org.accellera.ipxact.v1685_2014.volatile import Volatile

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class AlternateRegisters:
    """
    Alternate definitions for the current register.

    :ivar alternate_register: Alternate definition for the current
        register
    """

    class Meta:
        name = "alternateRegisters"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    alternate_register: Iterable["AlternateRegisters.AlternateRegister"] = (
        field(
            default_factory=list,
            metadata={
                "name": "alternateRegister",
                "type": "Element",
                "min_occurs": 1,
            },
        )
    )

    @dataclass(slots=True)
    class AlternateRegister:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar description:
        :ivar access_handles:
        :ivar is_present:
        :ivar alternate_groups: Defines a list of grouping names that
            this register description belongs.
        :ivar type_identifier: Identifier name used to indicate that
            multiple register elements contain the exact same
            information for the elements in the
            alternateRegisterDefinitionGroup.
        :ivar volatile:
        :ivar access:
        :ivar field_value: Describes individual bit fields within the
            register.
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
        description: Optional[Description] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        access_handles: Optional[
            "AlternateRegisters.AlternateRegister.AccessHandles"
        ] = field(
            default=None,
            metadata={
                "name": "accessHandles",
                "type": "Element",
            },
        )
        is_present: Optional[IsPresent] = field(
            default=None,
            metadata={
                "name": "isPresent",
                "type": "Element",
            },
        )
        alternate_groups: Optional[
            "AlternateRegisters.AlternateRegister.AlternateGroups"
        ] = field(
            default=None,
            metadata={
                "name": "alternateGroups",
                "type": "Element",
                "required": True,
            },
        )
        type_identifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "typeIdentifier",
                "type": "Element",
            },
        )
        volatile: Optional[Volatile] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        access: Optional[Access] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        field_value: Iterable[FieldType] = field(
            default_factory=list,
            metadata={
                "name": "field",
                "type": "Element",
                "min_occurs": 1,
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
            access_handle: Iterable[IndexedAccessHandle] = field(
                default_factory=list,
                metadata={
                    "name": "accessHandle",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

        @dataclass(slots=True)
        class AlternateGroups:
            """
            :ivar alternate_group: Defines a grouping name that this
                register description belongs.
            :ivar id:
            """

            alternate_group: Iterable[
                "AlternateRegisters.AlternateRegister.AlternateGroups.AlternateGroup"
            ] = field(
                default_factory=list,
                metadata={
                    "name": "alternateGroup",
                    "type": "Element",
                    "min_occurs": 1,
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
            class AlternateGroup:
                value: str = field(
                    default="",
                    metadata={
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
