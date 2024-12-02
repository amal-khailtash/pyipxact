from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_2.signal_constraints import SignalConstraints

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class SignalConstraintSets:
    """
    List of signalConstraints elements for a component signal.
    """

    class Meta:
        name = "signalConstraintSets"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    signal_constraints: Iterable[SignalConstraints] = field(
        default_factory=list,
        metadata={
            "name": "signalConstraints",
            "type": "Element",
            "min_occurs": 1,
        },
    )
