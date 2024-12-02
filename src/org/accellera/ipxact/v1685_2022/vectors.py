from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2022.vector import Vector

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Vectors:
    """
    Vectored information.
    """

    class Meta:
        name = "vectors"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    vector: Iterable[Vector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
