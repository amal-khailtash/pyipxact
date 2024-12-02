from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.port_access_type_value import (
    PortAccessTypeValue,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class PortAccessType:
    """Indicates how a netlister accesses a port.

    'ref' means accessed by reference (default) and 'ptr' means accessed
    by pointer.
    """

    class Meta:
        name = "portAccessType"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    value: Optional[PortAccessTypeValue] = field(default=None)
