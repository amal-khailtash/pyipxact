from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.dim import Dim
from org.accellera.ipxact.v1685_2022.stride import Stride

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Array:
    """
    :ivar dim: Dimensions a memory-map element array, the semantics for
        dim elements are the same as the C language standard for the
        layout of memory in multidimensional arrays.
    :ivar stride:
    """

    class Meta:
        name = "array"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    dim: Iterable[Dim] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    stride: Optional[Stride] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
