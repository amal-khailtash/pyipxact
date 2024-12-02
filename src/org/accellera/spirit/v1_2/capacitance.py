from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.capacitance_value_unit_type import (
    CapacitanceValueUnitType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class Capacitance:
    """
    Represents a simple capacitance value with optional units.
    """

    class Meta:
        name = "capacitance"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    units: Optional[CapacitanceValueUnitType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
