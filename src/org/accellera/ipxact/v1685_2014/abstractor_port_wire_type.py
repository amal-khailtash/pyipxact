from dataclasses import dataclass, field
from typing import Any

from org.accellera.ipxact.v1685_2014.port_wire_type import PortWireType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class AbstractorPortWireType(PortWireType):
    """
    Wire port type for an abstractor.
    """

    class Meta:
        name = "abstractorPortWireType"

    constraint_sets: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
