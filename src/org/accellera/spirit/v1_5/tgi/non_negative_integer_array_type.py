from dataclasses import dataclass, field
from typing import Any

from org.accellera.spirit.v1_5.tgi.array import Array

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class NonNegativeIntegerArrayType(Array):
    class Meta:
        name = "nonNegativeIntegerArrayType"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    other_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
