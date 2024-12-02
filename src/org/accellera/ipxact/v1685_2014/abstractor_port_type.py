from dataclasses import dataclass, field
from typing import Any

from org.accellera.ipxact.v1685_2014.port_type import PortType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class AbstractorPortType(PortType):
    """
    A port description, giving a name and an access type for high level ports.
    """

    class Meta:
        name = "abstractorPortType"

    arrays: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
