from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.ad_hoc_connections import (
    AdHocConnections,
)
from org.accellera.spirit.v1685_2009.ve.component_instances import (
    ComponentInstances,
)
from org.accellera.spirit.v1685_2009.ve.description import Description
from org.accellera.spirit.v1685_2009.ve.interconnections import (
    Interconnections,
)
from org.accellera.spirit.v1685_2009.ve.interface import Interface
from org.accellera.spirit.v1685_2009.ve.vendor_extensions import (
    VendorExtensions,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class Design:
    """
    Root element for a platform design.

    :ivar vendor: Name of the vendor who supplies this file.
    :ivar library: Name of the logical library this element belongs to.
    :ivar name: The name of the object.
    :ivar version: Indicates the version of the named element.
    :ivar component_instances:
    :ivar interconnections:
    :ivar ad_hoc_connections:
    :ivar hier_connections: A list of hierarchy connections between bus
        interfaces on component instances and the bus interfaces on the
        encompassing component.
    :ivar description:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "design"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

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
    description: Optional[Description] = field(
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
                    "min_occurs": 1,
                },
            )
        )

        @dataclass(slots=True)
        class HierConnection:
            """
            :ivar interface: Component and bus reference to export to
                the upper level component. The componentRef and busRef
                attributes indicate the instance name and bus interface
                name (active or monitor) of the hierachical connection.
            :ivar vendor_extensions:
            :ivar interface_ref: This is the name of the bus interface
                on the upper level component.
            """

            interface: Optional[Interface] = field(
                default=None,
                metadata={
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
            interface_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "interfaceRef",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    "required": True,
                },
            )
