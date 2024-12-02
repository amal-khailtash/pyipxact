from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.design_rule_constraints import (
    DesignRuleConstraints,
)
from org.accellera.spirit.v1_2.false_path import FalsePath
from org.accellera.spirit.v1_2.multi_cycle_path import MultiCyclePath
from org.accellera.spirit.v1_2.timed_path import TimedPath

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class ComponentConstraints:
    """Defines the set of implementation constraints associated with a component.

    If multiple componentConstraints elements are used, each must have a
    unique value for the constraintSet attribute.
    """

    class Meta:
        name = "componentConstraints"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    design_rule_constraints: Optional[DesignRuleConstraints] = field(
        default=None,
        metadata={
            "name": "designRuleConstraints",
            "type": "Element",
        },
    )
    false_path: Iterable[FalsePath] = field(
        default_factory=list,
        metadata={
            "name": "falsePath",
            "type": "Element",
        },
    )
    multi_cycle_path: Iterable[MultiCyclePath] = field(
        default_factory=list,
        metadata={
            "name": "multiCyclePath",
            "type": "Element",
        },
    )
    timed_path: Iterable[TimedPath] = field(
        default_factory=list,
        metadata={
            "name": "timedPath",
            "type": "Element",
        },
    )
    constraint_set_id: str = field(
        default="default",
        metadata={
            "name": "constraintSetId",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
