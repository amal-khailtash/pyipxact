from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.description import Description
from org.accellera.ipxact.v1685_2022.ipxact_uri import IpxactUri
from org.accellera.ipxact.v1685_2022.library_ref_type import LibraryRefType
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class IpxactFileType:
    """
    :ivar vlnv: VLNV of the IP-XACT file being cataloged.
    :ivar name: Name of the IP-XACT file being cataloged.
    :ivar description:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "ipxactFileType"

    vlnv: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    name: Optional[IpxactUri] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    description: Optional[Description] = field(
        default=None,
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
