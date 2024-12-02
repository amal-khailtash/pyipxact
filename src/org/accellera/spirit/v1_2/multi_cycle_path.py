from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.check_value_type import CheckValueType
from org.accellera.spirit.v1_2.edge_value_type import EdgeValueType
from org.accellera.spirit.v1_2.path_specifier import PathSpecifier
from org.accellera.spirit.v1_2.relative_clock_type import RelativeClockType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class MultiCyclePath:
    """
    Defines a multi-cycle path timing exception.
    """

    class Meta:
        name = "multiCyclePath"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    path_specifier: Optional[PathSpecifier] = field(
        default=None,
        metadata={
            "name": "pathSpecifier",
            "type": "Element",
            "required": True,
        },
    )
    cycles: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    path_edge: Optional[EdgeValueType] = field(
        default=None,
        metadata={
            "name": "pathEdge",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    path_type: Optional[CheckValueType] = field(
        default=None,
        metadata={
            "name": "pathType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    relative_clock: Optional[RelativeClockType] = field(
        default=None,
        metadata={
            "name": "relativeClock",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
