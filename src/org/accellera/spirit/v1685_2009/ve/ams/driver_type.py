from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.ams.clock_driver import ClockDriver
from org.accellera.spirit.v1685_2009.ve.ams.default_value import DefaultValue
from org.accellera.spirit.v1685_2009.ve.ams.single_shot_driver import (
    SingleShotDriver,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


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
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    clock_driver: Optional[ClockDriver] = field(
        default=None,
        metadata={
            "name": "clockDriver",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    single_shot_driver: Optional[SingleShotDriver] = field(
        default=None,
        metadata={
            "name": "singleShotDriver",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
