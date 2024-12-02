from dataclasses import dataclass, field
from typing import Any

from org.accellera.spirit.v1_4.port_wire_type import PortWireType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


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
