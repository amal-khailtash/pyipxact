from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_5.wire_type_def import WireTypeDef

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class WireTypeDefs:
    """The group of wire type definitions.

    If no match to a viewName is found then the default language types
    are to be used. See the User Guide for these default types.
    """

    class Meta:
        name = "wireTypeDefs"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

    wire_type_def: Iterable[WireTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "wireTypeDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )