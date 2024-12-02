from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.power.always_powered import (
    AlwaysPowered,
)
from org.accellera.spirit.v1685_2009.ve.power.domain import Domain
from org.accellera.spirit.v1685_2009.ve.power.has_isolation import HasIsolation
from org.accellera.spirit.v1685_2009.ve.power.has_level_shifter import (
    HasLevelShifter,
)
from org.accellera.spirit.v1685_2009.ve.power.idle import Idle
from org.accellera.spirit.v1685_2009.ve.power.isolation import Isolation
from org.accellera.spirit.v1685_2009.ve.power.reset import Reset
from org.accellera.spirit.v1685_2009.ve.power.retention_mode import (
    RetentionMode,
)

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0"
)


@dataclass(slots=True)
class ComponentPowerDef:
    """
    Power definition of a component.
    """

    class Meta:
        name = "componentPowerDef"
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
    retention_mode: Optional[RetentionMode] = field(
        default=None,
        metadata={
            "name": "retentionMode",
            "type": "Element",
        },
    )
    always_powered: Optional[AlwaysPowered] = field(
        default=None,
        metadata={
            "name": "alwaysPowered",
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
    has_isolation: Optional[HasIsolation] = field(
        default=None,
        metadata={
            "name": "hasIsolation",
            "type": "Element",
        },
    )
    has_level_shifter: Optional[HasLevelShifter] = field(
        default=None,
        metadata={
            "name": "hasLevelShifter",
            "type": "Element",
        },
    )
