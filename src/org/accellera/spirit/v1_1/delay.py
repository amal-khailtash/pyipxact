from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.delay_value_unit_type import DelayValueUnitType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class Delay:
    """
    Represents a simple delay value with optional units.
    """

    class Meta:
        name = "delay"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    units: Optional[DelayValueUnitType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
