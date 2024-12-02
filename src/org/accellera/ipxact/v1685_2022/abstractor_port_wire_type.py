from dataclasses import dataclass, field
from typing import Any

from org.accellera.ipxact.v1685_2022.port_wire_type import PortWireType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class AbstractorPortWireType(PortWireType):
    """
    Wire port type for an abstractor.

    :ivar constraint_sets:
    :ivar power_constraints: Wire port power constraints.
    """

    class Meta:
        name = "abstractorPortWireType"

    constraint_sets: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    power_constraints: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
