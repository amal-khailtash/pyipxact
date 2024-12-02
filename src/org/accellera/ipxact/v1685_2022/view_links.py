from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class ViewLinks:
    """
    A set of links between internal and external views defined in the
    typeDefinitions document.

    :ivar view_link: A link between one external view and one internal
        view.
    """

    class Meta:
        name = "viewLinks"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    view_link: Iterable["ViewLinks.ViewLink"] = field(
        default_factory=list,
        metadata={
            "name": "viewLink",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class ViewLink:
        """
        :ivar external_view_reference: Reference to a view defined in
            the linked external type definitions.
        :ivar view_reference: Reference to a view defined internally.
        :ivar vendor_extensions:
        :ivar id:
        """

        external_view_reference: Optional[
            "ViewLinks.ViewLink.ExternalViewReference"
        ] = field(
            default=None,
            metadata={
                "name": "externalViewReference",
                "type": "Element",
                "required": True,
            },
        )
        view_reference: Optional["ViewLinks.ViewLink.ViewReference"] = field(
            default=None,
            metadata={
                "name": "viewReference",
                "type": "Element",
                "required": True,
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
        class ExternalViewReference:
            """
            :ivar view_ref: Reference to a specific view.
            """

            view_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "viewRef",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass(slots=True)
        class ViewReference:
            """
            :ivar view_ref: Reference to a specific view.
            """

            view_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "viewRef",
                    "type": "Attribute",
                    "required": True,
                },
            )
