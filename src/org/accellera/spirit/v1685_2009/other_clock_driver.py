from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.clock_driver_type import ClockDriverType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class OtherClockDriver(ClockDriverType):
    """Describes a clock not directly associated with an input port.

    The clockSource attribute can be used on these clocks to indicate
    the actual clock source (e.g. an output port of a clock generator
    cell).

    :ivar clock_name: Indicates the name of the clock.
    :ivar clock_source: Indicates the name of the actual clock source
        (e.g. an output pin of a clock generator cell).
    """

    class Meta:
        name = "otherClockDriver"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    clock_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "clockName",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "required": True,
        },
    )
    clock_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "clockSource",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
