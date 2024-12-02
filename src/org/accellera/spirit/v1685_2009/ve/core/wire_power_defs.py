from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1685_2009.ve.core.wire_power_def import WirePowerDef

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0"
)


@dataclass(slots=True)
class WirePowerDefs:
    """
    Wire port power definitions.

    :ivar wire_power_def: Single wire port power definition.
    """

    class Meta:
        name = "wirePowerDefs"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0"
        )

    wire_power_def: Iterable[WirePowerDef] = field(
        default_factory=list,
        metadata={
            "name": "wirePowerDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
