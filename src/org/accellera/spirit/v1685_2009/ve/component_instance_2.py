from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.component_instance_power_def import (
    ComponentInstancePowerDef,
)
from org.accellera.spirit.v1685_2009.ve.wire_instance_power_defs import (
    WireInstancePowerDefs,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"


@dataclass(slots=True)
class ComponentInstance2:
    """
    Component instance extension.
    """

    class Meta:
        name = "componentInstance"
        namespace = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"

    component_instance_power_def: Optional[ComponentInstancePowerDef] = field(
        default=None,
        metadata={
            "name": "componentInstancePowerDef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0",
        },
    )
    wire_instance_power_defs: Optional[WireInstancePowerDefs] = field(
        default=None,
        metadata={
            "name": "wireInstancePowerDefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/POWER-1.0",
        },
    )
