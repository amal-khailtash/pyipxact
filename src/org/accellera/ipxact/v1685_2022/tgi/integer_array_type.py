from dataclasses import dataclass, field
from typing import Any

from org.accellera.ipxact.v1685_2022.tgi.array import Array

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


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
