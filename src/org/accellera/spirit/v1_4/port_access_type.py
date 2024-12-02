from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_4.port_access_type_value import (
    PortAccessTypeValue,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class PortAccessType:
    """
    If present, indicates how a netlister accesses a port or all the ports of a
    busInterface.
    """

    class Meta:
        name = "portAccessType"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"

    value: Optional[PortAccessTypeValue] = field(default=None)
