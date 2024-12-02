from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.ams.port_parameters import (
    PortParameters,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"


@dataclass(slots=True)
class Port2:
    """
    Port extension.
    """

    class Meta:
        name = "port"
        namespace = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"

    port_parameters: Optional[PortParameters] = field(
        default=None,
        metadata={
            "name": "portParameters",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/CORE-1.0",
        },
    )
