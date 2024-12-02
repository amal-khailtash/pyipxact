from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.resistance_value_unit_type import (
    ResistanceValueUnitType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class Resistance:
    """
    Represents a simple resistance value with optional units.
    """

    class Meta:
        name = "resistance"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 0.0,
        },
    )
    units: Optional[ResistanceValueUnitType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
