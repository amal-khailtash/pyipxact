from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.access import Access
from org.accellera.ipxact.v1685_2022.description import Description
from org.accellera.ipxact.v1685_2022.display_name import DisplayName
from org.accellera.ipxact.v1685_2022.modified_write_value import (
    ModifiedWriteValue,
)
from org.accellera.ipxact.v1685_2022.read_action import ReadAction
from org.accellera.ipxact.v1685_2022.read_response import ReadResponse
from org.accellera.ipxact.v1685_2022.short_description import ShortDescription
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions
from org.accellera.ipxact.v1685_2022.write_value_constraint import (
    WriteValueConstraint,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class FieldAccessPolicyDefinitions:
    class Meta:
        name = "fieldAccessPolicyDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    field_access_policy_definition: Iterable[
        "FieldAccessPolicyDefinitions.FieldAccessPolicyDefinition"
    ] = field(
        default_factory=list,
        metadata={
            "name": "fieldAccessPolicyDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class FieldAccessPolicyDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar access:
        :ivar modified_write_value:
        :ivar write_value_constraint:
        :ivar read_action:
        :ivar read_response:
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
