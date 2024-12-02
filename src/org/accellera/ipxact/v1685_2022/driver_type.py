from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.clock_driver import ClockDriver
from org.accellera.ipxact.v1685_2022.default_value import DefaultValue
from org.accellera.ipxact.v1685_2022.range import Range
from org.accellera.ipxact.v1685_2022.single_shot_driver import SingleShotDriver

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class DriverType:
    """
    Wire port driver type.

    :ivar range:
    :ivar view_ref: A reference to a view in the file for which this
        type applies.
    :ivar default_value:
    :ivar clock_driver:
    :ivar single_shot_driver:
    :ivar id:
    """

    class Meta:
        name = "driverType"

    range: Optional[Range] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    view_ref: Iterable["DriverType.ViewRef"] = field(
        default_factory=list,
        metadata={
            "name": "viewRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    default_value: Optional[DefaultValue] = field(
        default=None,
        metadata={
            "name": "defaultValue",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    clock_driver: Optional[ClockDriver] = field(
        default=None,
        metadata={
            "name": "clockDriver",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    single_shot_driver: Optional[SingleShotDriver] = field(
        default=None,
        metadata={
            "name": "singleShotDriver",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass(slots=True)
    class ViewRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
