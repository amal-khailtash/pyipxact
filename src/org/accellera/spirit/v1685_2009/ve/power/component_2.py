from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.power.component_power_def import (
    ComponentPowerDef,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"


@dataclass(slots=True)
class Component2:
    """
    Component extension.
    """

    class Meta:
        name = "component"
        namespace = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"

    component_power_def: Optional[ComponentPowerDef] = field(
        default=None,
        metadata={
            "name": "componentPowerDef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0",
        },
    )
