from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_4.initiative import Initiative
from org.accellera.spirit.v1_4.port_access_handle import PortAccessHandle
from org.accellera.spirit.v1_4.port_access_type import PortAccessType
from org.accellera.spirit.v1_4.service_type_defs import ServiceTypeDefs
from org.accellera.spirit.v1_4.trans_type_def import TransTypeDef
from org.accellera.spirit.v1_4.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class PortTransactionalType:
    """
    Transactional port type.

    :ivar trans_type_def: Definition of the port type expressed in the
        default language for this port (i.e. SystemC or SystemV).
    :ivar service: Describes the interface protocol.
    :ivar access: port access mode
    :ivar connection: Bounds number of legal connections.
    :ivar all_logical_initiatives_allowed: True if logical ports with
        different initiatives from the physical port initiative may be
        mapped onto this port. Forbidden for phantom ports, which always
        allow logical ports with all initiatives value to be mapped onto
        the physical port. Also ignored for "both" ports, since any
        logical port may be mapped to a physical "both" port.
    """

    class Meta:
        name = "portTransactionalType"

    trans_type_def: Optional[TransTypeDef] = field(
        default=None,
        metadata={
            "name": "transTypeDef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
    service: Optional["PortTransactionalType.Service"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            "required": True,
        },
    )
    access: Optional["PortTransactionalType.Access"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
    connection: Optional["PortTransactionalType.Connection"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )
    all_logical_initiatives_allowed: bool = field(
        default=False,
        metadata={
            "name": "allLogicalInitiativesAllowed",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
        },
    )

    @dataclass(slots=True)
    class Service:
        """
        :ivar initiative: Defines how the port accesses this service.
        :ivar service_type_defs: The group of service type definitions.
        :ivar vendor_extensions:
        """

        initiative: Optional[Initiative] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
                "required": True,
            },
        )
        service_type_defs: Optional[ServiceTypeDefs] = field(
            default=None,
            metadata={
                "name": "serviceTypeDefs",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            },
        )
        vendor_extensions: Optional[VendorExtensions] = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            },
        )

    @dataclass(slots=True)
    class Access:
        port_access_type: Optional[PortAccessType] = field(
            default=None,
            metadata={
                "name": "portAccessType",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            },
        )
        port_access_handle: Optional[PortAccessHandle] = field(
            default=None,
            metadata={
                "name": "portAccessHandle",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            },
        )

    @dataclass(slots=True)
    class Connection:
        """
        :ivar max_connections: Indicates the maximum number of
            connections this port supports. If this element is not
            present or set to 0 it implies an unbounded number of
            allowed connections.
        :ivar min_connections: Indicates the minimum number of
            connections this port supports. If this element is not
            present, the minimum number of allowed connections is 1.
        """

        max_connections: Optional[int] = field(
            default=None,
            metadata={
                "name": "maxConnections",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            },
        )
        min_connections: Optional[int] = field(
            default=None,
            metadata={
                "name": "minConnections",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            },
        )