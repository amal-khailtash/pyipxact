from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.core.interface import Interface

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class HierInterface(Interface):
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
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "white_space": "collapse",
            "pattern": r"\i[\p{L}\p{N}\.\-:_]*|\i[\p{L}\p{N}\.\-:_]*/\i[\p{L}\p{N}\.\-:_]*|(\i[\p{L}\p{N}\.\-:_]*/)+[\i\p{L}\p{N}\.\-:_]*",
        },
    )
