from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_4.interconnection import Interconnection
from org.accellera.spirit.v1_4.monitor_interconnection import (
    MonitorInterconnection,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class Interconnections:
    """
    Connections between internal sub components.
    """

    class Meta:
        name = "interconnections"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"

    interconnection: Iterable[Interconnection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    monitor_interconnection: Iterable[MonitorInterconnection] = field(
        default_factory=list,
        metadata={
            "name": "monitorInterconnection",
            "type": "Element",
        },
    )