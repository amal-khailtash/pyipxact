from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.domain import Domain
from org.accellera.spirit.v1685_2009.ve.has_isolation import HasIsolation
from org.accellera.spirit.v1685_2009.ve.has_level_shifter import (
    HasLevelShifter,
)
from org.accellera.spirit.v1685_2009.ve.idle import Idle
from org.accellera.spirit.v1685_2009.ve.isolation import Isolation
from org.accellera.spirit.v1685_2009.ve.name_ref import NameRef
from org.accellera.spirit.v1685_2009.ve.reset import Reset
from org.accellera.spirit.v1685_2009.ve.vector import Vector

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0"
)


@dataclass(slots=True)
class WireInstancePowerDef:
    """
    Component instance wire port power definition.
    """

    class Meta:
        name = "wireInstancePowerDef"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0"
        )

    name_ref: Optional[NameRef] = field(
        default=None,
        metadata={
            "name": "nameRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE",
            "required": True,
        },
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
    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )