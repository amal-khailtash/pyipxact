from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.ams.logical_wire_power_defs import (
    LogicalWirePowerDefs,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"


@dataclass(slots=True)
class LogicalWire:
    """
    Logical wire extension.
    """

    class Meta:
        name = "logicalWire"
        namespace = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"

    logical_wire_power_defs: Optional[LogicalWirePowerDefs] = field(
        default=None,
        metadata={
            "name": "logicalWirePowerDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0",
        },
    )
