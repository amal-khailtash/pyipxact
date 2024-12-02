from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.pdp.name_ref import NameRef
from org.accellera.spirit.v1685_2009.ve.pdp.vector import Vector

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0"
)


@dataclass(slots=True)
class NameRefVectorPair:
    class Meta:
        name = "nameRefVectorPair"

    name_ref: Optional[NameRef] = field(
        default=None,
        metadata={
            "name": "nameRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE",
            "required": True,
        },
    )
    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
