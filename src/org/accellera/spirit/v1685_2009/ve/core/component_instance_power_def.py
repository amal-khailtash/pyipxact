from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.core.always_powered import (
    AlwaysPowered,
)
from org.accellera.spirit.v1685_2009.ve.core.domain import Domain
from org.accellera.spirit.v1685_2009.ve.core.has_isolation import HasIsolation
from org.accellera.spirit.v1685_2009.ve.core.has_level_shifter import (
    HasLevelShifter,
)
from org.accellera.spirit.v1685_2009.ve.core.idle import Idle
from org.accellera.spirit.v1685_2009.ve.core.isolation import Isolation
from org.accellera.spirit.v1685_2009.ve.core.reset import Reset
from org.accellera.spirit.v1685_2009.ve.core.retention_mode import (
    RetentionMode,
)

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0"
)


@dataclass(slots=True)
class ComponentInstancePowerDef:
    """
    Component instance power definition.
    """

    class Meta:
        name = "componentInstancePowerDef"
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
