from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.left import Left
from org.accellera.ipxact.v1685_2014.right import Right

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ConfigurableArrays:
    """
    :ivar array: Specific left and right array bounds.
    """

    class Meta:
        name = "configurableArrays"

    array: Iterable["ConfigurableArrays.Array"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class Array:
        left: Optional[Left] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                "required": True,
            },
        )
        right: Optional[Right] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                "required": True,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )