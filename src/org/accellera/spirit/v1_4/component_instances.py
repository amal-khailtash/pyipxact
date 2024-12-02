from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_4.component_instance import ComponentInstance

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class ComponentInstances:
    """
    Sub instances of internal components.
    """

    class Meta:
        name = "componentInstances"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"

    component_instance: Iterable[ComponentInstance] = field(
        default_factory=list,
        metadata={
            "name": "componentInstance",
            "type": "Element",
            "min_occurs": 1,
        },
    )
