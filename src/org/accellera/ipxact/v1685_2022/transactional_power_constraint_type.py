from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.power_domain_ref import PowerDomainRef
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class TransactionalPowerConstraintType:
    class Meta:
        name = "transactionalPowerConstraintType"

    power_domain_ref: Optional[PowerDomainRef] = field(
        default=None,
        metadata={
            "name": "powerDomainRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
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