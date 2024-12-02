from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.component_port_direction_type import (
    ComponentPortDirectionType,
)
from org.accellera.ipxact.v1685_2014.constraint_sets import ConstraintSets
from org.accellera.ipxact.v1685_2014.drivers import Drivers
from org.accellera.ipxact.v1685_2014.vectors import Vectors
from org.accellera.ipxact.v1685_2014.wire_type_defs import WireTypeDefs

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class PortWireType:
    """
    Wire port type for a component.

    :ivar direction: The direction of a wire style port. The basic
        directions for a port are 'in' for input ports, 'out' for output
        port and 'inout' for bidirectional and tristate ports. A value
        of 'phantom' is also allowed and define a port that exist on the
        IP-XACT component but not on the HDL model.
    :ivar vectors:
    :ivar wire_type_defs:
    :ivar drivers:
    :ivar constraint_sets:
    :ivar all_logical_directions_allowed: True if logical ports with
        different directions from the physical port direction may be
        mapped onto this port. Forbidden for phantom ports, which always
        allow logical ports with all direction value to be mapped onto
        the physical port. Also ignored for inout ports, since any
        logical port maybe mapped to a physical inout port.
    """

    class Meta:
        name = "portWireType"

    direction: Optional[ComponentPortDirectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "required": True,
        },
    )
    vectors: Optional[Vectors] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    wire_type_defs: Optional[WireTypeDefs] = field(
        default=None,
        metadata={
            "name": "wireTypeDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    drivers: Optional[Drivers] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    constraint_sets: Optional[ConstraintSets] = field(
        default=None,
        metadata={
            "name": "constraintSets",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    all_logical_directions_allowed: bool = field(
        default=False,
        metadata={
            "name": "allLogicalDirectionsAllowed",
            "type": "Attribute",
        },
    )
