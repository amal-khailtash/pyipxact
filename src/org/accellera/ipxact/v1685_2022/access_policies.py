from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.access_type import AccessType
from org.accellera.ipxact.v1685_2022.mode_ref import ModeRef
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class AccessPolicies:
    class Meta:
        name = "accessPolicies"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    access_policy: Iterable["AccessPolicies.AccessPolicy"] = field(
        default_factory=list,
        metadata={
            "name": "accessPolicy",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class AccessPolicy:
        mode_ref: Iterable[ModeRef] = field(
            default_factory=list,
            metadata={
                "name": "modeRef",
                "type": "Element",
            },
        )
        access: Optional[AccessType] = field(
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
