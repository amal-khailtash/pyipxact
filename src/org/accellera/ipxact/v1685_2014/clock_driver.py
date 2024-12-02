from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.clock_driver_type import ClockDriverType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ClockDriver(ClockDriverType):
    """
    Describes a driven clock port.

    :ivar clock_name: Indicates the name of the cllock. If not specified
        the name is assumed to be the name of the containing port.
    """

    class Meta:
        name = "clockDriver"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    clock_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "clockName",
            "type": "Attribute",
        },
    )
