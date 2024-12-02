from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.interface_type import InterfaceType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class HierInterface(InterfaceType):
    """
    Hierarchical reference to an interface.

    :ivar path: A decending hierarchical (slash separated - example
        x/y/z) path to the component instance containing the specified
        component instance in componentRef. If not specified the
        componentRef instance shall exist in the current design.
    """

    class Meta:
        name = "hierInterface"

    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*|\i[\p{L}\p{N}\.\-:_]*/\i[\p{L}\p{N}\.\-:_]*|(\i[\p{L}\p{N}\.\-:_]*/)+[\i\p{L}\p{N}\.\-:_]*",
        },
    )
