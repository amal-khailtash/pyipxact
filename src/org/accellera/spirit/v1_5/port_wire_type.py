from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_5.component_port_direction_type import (
    ComponentPortDirectionType,
)
from org.accellera.spirit.v1_5.constraint_sets import ConstraintSets
from org.accellera.spirit.v1_5.driver import Driver
from org.accellera.spirit.v1_5.vector import Vector
from org.accellera.spirit.v1_5.wire_type_defs import WireTypeDefs

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class PortWireType:
    """
    Wire port type for a component.

    :ivar direction: The direction of a wire style port. The basic
        directions for a port are 'in' for input ports, 'out' for output
        port and 'inout' for bidirectional and tristate ports. A value
        of 'phantom' is also allowed and define a port that exist on the
        IP-XACT component but not on the HDL model.
    :ivar vector: Specific left and right vector bounds. Signal width is
        max(left,right)-min(left,right)+1 When the bounds are not
        present, a scalar port is assumed.
    :ivar wire_type_defs:
    :ivar driver:
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
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    wire_type_defs: Optional[WireTypeDefs] = field(
        default=None,
        metadata={
            "name": "wireTypeDefs",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    driver: Optional[Driver] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    constraint_sets: Optional[ConstraintSets] = field(
        default=None,
        metadata={
            "name": "constraintSets",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    all_logical_directions_allowed: bool = field(
        default=False,
        metadata={
            "name": "allLogicalDirectionsAllowed",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
