from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.left import Left
from org.accellera.ipxact.v1685_2014.right import Right

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Vector:
    """
    Left and right ranges of the vector.
    """

    class Meta:
        name = "vector"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    left: Optional[Left] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    right: Optional[Right] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
