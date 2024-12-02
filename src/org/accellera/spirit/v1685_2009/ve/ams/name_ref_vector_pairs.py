from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1685_2009.ve.ams.name_ref_vector_pair import (
    NameRefVectorPair,
)

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0"
)


@dataclass(slots=True)
class NameRefVectorPairs:
    class Meta:
        name = "nameRefVectorPairs"

    source: Iterable[NameRefVectorPair] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0",
            "min_occurs": 1,
        },
    )
