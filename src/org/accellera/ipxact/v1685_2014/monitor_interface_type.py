from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.description import Description
from org.accellera.ipxact.v1685_2014.interface_type import InterfaceType
from org.accellera.ipxact.v1685_2014.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class MonitorInterfaceType(InterfaceType):
    """
    Hierarchical reference to an interface being monitored or monitoring another
    interface.

    :ivar description:
    :ivar vendor_extensions:
    :ivar path: A decending hierarchical (slash separated - example
        x/y/z) path to the component instance containing the specified
        component instance in componentRef. If not specified the
        componentRef instance shall exist in the current design.
    """

    class Meta:
        name = "monitorInterfaceType"

    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    path: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )