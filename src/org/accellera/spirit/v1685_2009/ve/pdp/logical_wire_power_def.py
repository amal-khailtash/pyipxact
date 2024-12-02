from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.pdp.domain import Domain
from org.accellera.spirit.v1685_2009.ve.pdp.idle import Idle
from org.accellera.spirit.v1685_2009.ve.pdp.isolation import Isolation
from org.accellera.spirit.v1685_2009.ve.pdp.reset import Reset
from org.accellera.spirit.v1685_2009.ve.pdp.vector import Vector

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0"
)


@dataclass(slots=True)
class LogicalWirePowerDef:
    """
    Logical wire port power definition.
    """

    class Meta:
        name = "logicalWirePowerDef"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0"
        )

    domain: Optional[Domain] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    isolation: Optional[Isolation] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    idle: Optional[Idle] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reset: Optional[Reset] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
