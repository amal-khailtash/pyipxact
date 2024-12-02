from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.arrays import Arrays
from org.accellera.ipxact.v1685_2022.component_port_direction_type import (
    ComponentPortDirectionType,
)
from org.accellera.ipxact.v1685_2022.description import Description
from org.accellera.ipxact.v1685_2022.display_name import DisplayName
from org.accellera.ipxact.v1685_2022.extended_vectors_type import (
    ExtendedVectorsType,
)
from org.accellera.ipxact.v1685_2022.port_access_type import PortAccessType
from org.accellera.ipxact.v1685_2022.port_wire_type import PortWireType
from org.accellera.ipxact.v1685_2022.short_description import ShortDescription
from org.accellera.ipxact.v1685_2022.struct_port_type_defs import (
    StructPortTypeDefs,
)
from org.accellera.ipxact.v1685_2022.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class SubPortType:
    """
    A port description, giving a name and an access type for high level ports.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar wire: Defines a port whose type resolves to simple bits.
    :ivar structured:
    :ivar arrays:
    :ivar access: Port access characteristics.
    :ivar vendor_extensions:
    :ivar id:
    :ivar is_io: When present and set to 'true' identifies this port as
        being an I/O to the containing structure port type.  Only valid
        for subPorts contained in a structured port with
        structType='interface'.
    """

    class Meta:
        name = "subPortType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*",
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    wire: Optional[PortWireType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    structured: Optional["PortStructuredType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    arrays: Optional[Arrays] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    access: Optional[PortAccessType] = field(
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
    is_io: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isIO",
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class PortStructuredType:
    """
    :ivar struct:
    :ivar union:
    :ivar interface:
    :ivar vectors: Vectored information.
    :ivar sub_ports:
    :ivar struct_port_type_defs:
    :ivar packed: When not present or set to 'true' indicates that this
        structured port is 'packed'.  If present and set to 'false',
        indicates that this structured port is 'unpacked'.
    """

    class Meta:
        name = "portStructuredType"

    struct: Optional["PortStructuredType.Struct"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    union: Optional["PortStructuredType.UnionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    interface: Optional["PortStructuredType.Interface"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vectors: Optional[ExtendedVectorsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    sub_ports: Optional["PortStructuredType.SubPorts"] = field(
        default=None,
        metadata={
            "name": "subPorts",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    struct_port_type_defs: Optional[StructPortTypeDefs] = field(
        default=None,
        metadata={
            "name": "structPortTypeDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    packed: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(slots=True)
    class SubPorts:
        sub_port: Iterable[SubPortType] = field(
            default_factory=list,
            metadata={
                "name": "subPort",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

    @dataclass(slots=True)
    class Struct:
        """
        :ivar direction: The direction of a wire style port. The basic
            directions for a port are 'in' for input ports, 'out' for
            output port and 'inout' for bidirectional and tristate
            ports. A value of 'phantom' is also allowed and define a
            port that exist on the IP-XACT component but not on the HDL
            model.
        """

        direction: Optional[ComponentPortDirectionType] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(slots=True)
    class UnionType:
        """
        :ivar direction: The direction of a wire style port. The basic
            directions for a port are 'in' for input ports, 'out' for
            output port and 'inout' for bidirectional and tristate
            ports. A value of 'phantom' is also allowed and define a
            port that exist on the IP-XACT component but not on the HDL
            model.
        """

        direction: Optional[ComponentPortDirectionType] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(slots=True)
    class Interface:
        phantom: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
