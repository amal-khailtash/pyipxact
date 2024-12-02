from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2014.requires_driver_driver_type import (
    RequiresDriverDriverType,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class RequiresDriver:
    """Specifies if a port requires a driver.

    Default is false. The attribute driverType can further qualify what
    type of driver is required. Undefined behaviour if direction is not
    input or inout. Driver type any indicates that any unspecified type
    of driver must be connected

    :ivar value:
    :ivar driver_type: Defines the type of driver that is required. The
        default is any type of driver. The 2 other options are a clock
        type driver or a singleshot type driver.
    """

    class Meta:
        name = "requiresDriver"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )
    driver_type: RequiresDriverDriverType = field(
        default=RequiresDriverDriverType.ANY,
        metadata={
            "name": "driverType",
            "type": "Attribute",
        },
    )
