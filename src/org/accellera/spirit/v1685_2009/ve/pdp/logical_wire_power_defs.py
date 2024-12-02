from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1685_2009.ve.pdp.logical_wire_power_def import (
    LogicalWirePowerDef,
)

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0"
)


@dataclass(slots=True)
class LogicalWirePowerDefs:
    """
    Logical wire port power definitions.

    :ivar logical_wire_power_def: Single logical wire port power
        definition.
    """

    class Meta:
        name = "logicalWirePowerDefs"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0"
        )

    logical_wire_power_def: Iterable[LogicalWirePowerDef] = field(
        default_factory=list,
        metadata={
            "name": "logicalWirePowerDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
