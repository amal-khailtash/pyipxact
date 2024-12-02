from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_1.clock_driver import ClockDriver

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class OtherClocks:
    """List of clocks associated with the component that are not associated with
    signals.

    Set the clockSource attribute on the clockDriver to indicate the
    source of a clock not associated with a particular component signal.
    """

    class Meta:
        name = "otherClocks"

    clock_driver: Iterable[ClockDriver] = field(
        default_factory=list,
        metadata={
            "name": "clockDriver",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            "min_occurs": 1,
        },
    )
