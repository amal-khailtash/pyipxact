from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.left import Left
from org.accellera.ipxact.v1685_2022.right import Right

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Range:
    """
    Left and right bound of a reference into a vector.
    """

    class Meta:
        name = "range"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

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
