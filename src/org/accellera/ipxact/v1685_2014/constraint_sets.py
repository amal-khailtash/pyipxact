from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2014.constraint_set import ConstraintSet

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ConstraintSets:
    """
    List of constraintSet elements for a component port.
    """

    class Meta:
        name = "constraintSets"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    constraint_set: Iterable[ConstraintSet] = field(
        default_factory=list,
        metadata={
            "name": "constraintSet",
            "type": "Element",
            "min_occurs": 1,
        },
    )
