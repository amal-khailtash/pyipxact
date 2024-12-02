from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.clock_driver import ClockDriver
from org.accellera.ipxact.v1685_2014.default_value import DefaultValue
from org.accellera.ipxact.v1685_2014.range import Range
from org.accellera.ipxact.v1685_2014.single_shot_driver import SingleShotDriver

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class DriverType:
    """
    Wire port driver type.
    """

    class Meta:
        name = "driverType"

    range: Optional[Range] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    default_value: Optional[DefaultValue] = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    clock_driver: Optional[ClockDriver] = field(
        default=None,
        metadata={
            "name": "clockDriver",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    single_shot_driver: Optional[SingleShotDriver] = field(
        default=None,
        metadata={
            "name": "singleShotDriver",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
