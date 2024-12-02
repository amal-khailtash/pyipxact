from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_2.component_constraints import (
    ComponentConstraints,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class ComponentConstraintSets:
    """
    List of componentConstraints elements for this component.
    """

    class Meta:
        name = "componentConstraintSets"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    component_constraints: Iterable[ComponentConstraints] = field(
        default_factory=list,
        metadata={
            "name": "componentConstraints",
            "type": "Element",
            "min_occurs": 1,
        },
    )
