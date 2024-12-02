from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_4.other_clock_driver import OtherClockDriver

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class OtherClocks:
    """List of clocks associated with the component that are not associated with
    ports.

    Set the clockSource attribute on the clockDriver to indicate the
    source of a clock not associated with a particular component port.
    """

    class Meta:
        name = "otherClocks"

    other_clock_driver: Iterable[OtherClockDriver] = field(
        default_factory=list,
        metadata={
            "name": "otherClockDriver",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            "min_occurs": 1,
        },
    )
