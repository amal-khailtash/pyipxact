from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.slices_type import SlicesType
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class ClearboxElementRefType:
    """Reference to a clearboxElement within a view.

    The 'name' attribute must refer to a clearboxElement defined within
    this component.

    :ivar location: The contents of each location element can be used to
        specified one location (HDL Path) through the referenced
        clearBoxElement is accessible.
    :ivar vendor_extensions:
    :ivar name: Reference to a clearboxElement defined within this
        component.
    :ivar id:
    """

    class Meta:
        name = "clearboxElementRefType"

    location: Iterable[SlicesType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "min_occurs": 1,
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
