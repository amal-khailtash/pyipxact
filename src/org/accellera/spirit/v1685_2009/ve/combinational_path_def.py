from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.name_ref_vector_pairs import (
    NameRefVectorPairs,
)
from org.accellera.spirit.v1685_2009.ve.vector import Vector

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0"
)


@dataclass(slots=True)
class CombinationalPathDef:
    class Meta:
        name = "combinationalPathDef"

    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    sources: Optional[NameRefVectorPairs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0",
            "required": True,
        },
    )
