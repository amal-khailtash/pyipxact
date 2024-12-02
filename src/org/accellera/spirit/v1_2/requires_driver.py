from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.requires_driver_driver_type import (
    RequiresDriverDriverType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class RequiresDriver:
    """Specifies if a signal requires a driver.

    Default is false. The attribute driverType can further qualify what
    type of driver is required. Undefined behaviour if direction is not
    input or inout. Driver type any indicates that any unspecified type
    of driver must be connected
    """

    class Meta:
        name = "requiresDriver"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    driver_type: RequiresDriverDriverType = field(
        default=RequiresDriverDriverType.ANY,
        metadata={
            "name": "driverType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
