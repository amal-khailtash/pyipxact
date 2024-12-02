from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_1.bus_def_signal_constraints import (
    BusDefSignalConstraints,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class BusDefSignalConstraintSets:
    """
    List of busDefSignalConstraints elements for a bus definition signal.
    """

    class Meta:
        name = "busDefSignalConstraintSets"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    bus_def_signal_constraints: Iterable[BusDefSignalConstraints] = field(
        default_factory=list,
        metadata={
            "name": "busDefSignalConstraints",
            "type": "Element",
            "min_occurs": 1,
        },
    )
