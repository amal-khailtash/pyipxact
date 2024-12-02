from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.pdp.clock_driver_type import (
    ClockDriverType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class ClockDriver(ClockDriverType):
    """
    Describes a driven clock port.

    :ivar clock_name: Indicates the name of the cllock. If not specified
        the name is assumed to be the name of the containing port.
    """

    class Meta:
        name = "clockDriver"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    clock_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "clockName",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
