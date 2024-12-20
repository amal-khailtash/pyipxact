from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.simple_port_access_type import (
    SimplePortAccessType,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class PortAccessType:
    """Indicates how a netlister accesses a port.

    'ref' means accessed by reference (default) and 'ptr' means accessed
    by pointer.
    """

    class Meta:
        name = "portAccessType"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: Optional[SimplePortAccessType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
