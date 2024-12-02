from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.ad_hoc_connections import AdHocConnections
from org.accellera.spirit.v1_2.component_instances import ComponentInstances
from org.accellera.spirit.v1_2.interconnections import Interconnections
from org.accellera.spirit.v1_2.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class Design:
    """
    Root element for a platform design.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version:
    :ivar component_instances:
    :ivar interconnections:
    :ivar ad_hoc_connections:
    :ivar hier_connections: A list of hierarchy connections between bus
        interfaces on component instances and the bus interfaces on the
        encompassing component.
    :ivar vendor_extensions:
    """

    class Meta:
        name = "design"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    vendor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    library: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    component_instances: Optional[ComponentInstances] = field(
        default=None,
        metadata={
            "name": "componentInstances",
            "type": "Element",
        },
    )
    interconnections: Optional[Interconnections] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ad_hoc_connections: Optional[AdHocConnections] = field(
        default=None,
        metadata={
            "name": "adHocConnections",
            "type": "Element",
        },
    )
    hier_connections: Optional["Design.HierConnections"] = field(
        default=None,
        metadata={
            "name": "hierConnections",
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

    @dataclass(slots=True)
    class HierConnections:
        """
        :ivar hier_connection: Represents a hierarchy connection
        """

        hier_connection: Iterable["Design.HierConnections.HierConnection"] = (
            field(
                default_factory=list,
                metadata={
                    "name": "hierConnection",
                    "type": "Element",
                },
            )
        )

        @dataclass(slots=True)
        class HierConnection:
            """
            :ivar component_ref: This is the instance name of the
                component which owns the busInterface that is to be
                exported
            :ivar interface_ref: This is the name of the bus interface
                on the instance
            :ivar vendor_extensions:
            :ivar interface_name: This is the name of the bus interface
                on the upper level component.
            """

            component_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "componentRef",
                    "type": "Element",
                    "required": True,
                },
            )
            interface_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "interfaceRef",
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
            interface_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "interfaceName",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                    "required": True,
                },
            )
