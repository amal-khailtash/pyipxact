from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_0.group_selector_multiple_group_selection_operator import (
    GroupSelectorMultipleGroupSelectionOperator,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class GroupSelector:
    """Specifies a set of group names used to select subsequent generators.

    The attribute "multipleGroupOperator" specifies the OR or AND
    selection operator if there is more than one group name
    (default=OR).

    :ivar name: Name used to select a generator or generator chain.
    :ivar multiple_group_selection_operator:
    """

    class Meta:
        name = "groupSelector"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"

    name: Iterable[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    multiple_group_selection_operator: GroupSelectorMultipleGroupSelectionOperator = field(
        default=GroupSelectorMultipleGroupSelectionOperator.OR,
        metadata={
            "name": "multipleGroupSelectionOperator",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
