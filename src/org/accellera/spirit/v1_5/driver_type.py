from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_5.clock_driver import ClockDriver
from org.accellera.spirit.v1_5.default_value import DefaultValue
from org.accellera.spirit.v1_5.single_shot_driver import SingleShotDriver

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class DriverType:
    """
    Wire port driver type.
    """

    class Meta:
        name = "driverType"

    default_value: Optional[DefaultValue] = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    clock_driver: Optional[ClockDriver] = field(
        default=None,
        metadata={
            "name": "clockDriver",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    single_shot_driver: Optional[SingleShotDriver] = field(
        default=None,
        metadata={
            "name": "singleShotDriver",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
