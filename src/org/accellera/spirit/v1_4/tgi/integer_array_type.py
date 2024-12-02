from dataclasses import dataclass, field
from typing import Any

from org.accellera.spirit.v1_4.tgi.array import Array

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class IntegerArrayType(Array):
    class Meta:
        name = "integerArrayType"

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
