from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_1.interconnection import Interconnection

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class Interconnections:
    """
    Connections between internal sub components.
    """

    class Meta:
        name = "interconnections"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    interconnection: Iterable[Interconnection] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )