from dataclasses import dataclass, field
from typing import Any

from org.accellera.spirit.v1685_2009.ve.power.port_wire_type import (
    PortWireType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


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