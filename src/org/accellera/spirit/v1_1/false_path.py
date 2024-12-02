from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.check_value_type import CheckValueType
from org.accellera.spirit.v1_1.edge_value_type import EdgeValueType
from org.accellera.spirit.v1_1.path_specifier import PathSpecifier

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class FalsePath:
    """
    Defines a false path timing exception.
    """

    class Meta:
        name = "falsePath"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    path_specifier: Optional[PathSpecifier] = field(
        default=None,
        metadata={
            "name": "pathSpecifier",
            "type": "Element",
            "required": True,
        },
    )
    path_edge: Optional[EdgeValueType] = field(
        default=None,
        metadata={
            "name": "pathEdge",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    path_type: Optional[CheckValueType] = field(
        default=None,
        metadata={
            "name": "pathType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
