from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.core.port_access_handle import (
    PortAccessHandle,
)
from org.accellera.spirit.v1685_2009.ve.core.port_access_type import (
    PortAccessType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class PortAccessType1:
    """
    :ivar port_access_type: Indicates how a netlister accesses a port.
        'ref' means accessed by reference (default) and 'ptr' means
        accessed through a pointer.
    :ivar port_access_handle:
    """

    class Meta:
        name = "portAccessType"

    port_access_type: Optional[PortAccessType] = field(
        default=None,
        metadata={
            "name": "portAccessType",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    port_access_handle: Optional[PortAccessHandle] = field(
        default=None,
        metadata={
            "name": "portAccessHandle",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
