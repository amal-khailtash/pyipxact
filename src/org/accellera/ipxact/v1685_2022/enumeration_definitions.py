from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.description import Description
from org.accellera.ipxact.v1685_2022.display_name import DisplayName
from org.accellera.ipxact.v1685_2022.enumerated_value_type import (
    EnumeratedValueType,
)
from org.accellera.ipxact.v1685_2022.short_description import ShortDescription
from org.accellera.ipxact.v1685_2022.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class EnumerationDefinitions:
    class Meta:
        name = "enumerationDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    enumeration_definition: Iterable[
        "EnumerationDefinitions.EnumerationDefinition"
    ] = field(
        default_factory=list,
        metadata={
            "name": "enumerationDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class EnumerationDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar width: Definition width used to resolve the value.
        :ivar enumerated_value: Enumerates specific values that can be
            assigned to the bit field. The name of this enumerated
            value. This may be used as a token in generating code.
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
        width: Optional[UnsignedPositiveIntExpression] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        enumerated_value: Iterable[EnumeratedValueType] = field(
            default_factory=list,
            metadata={
                "name": "enumeratedValue",
                "type": "Element",
                "min_occurs": 1,
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
