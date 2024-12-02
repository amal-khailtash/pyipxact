from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.ve.is_present import IsPresent

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022-VE"


@dataclass(slots=True)
class ActiveInterface:
    """
    ActiveInterface isPresent extension.
    """

    class Meta:
        name = "activeInterface"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022-VE"

    is_present: Optional[IsPresent] = field(
        default=None,
        metadata={
            "name": "isPresent",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022-VE/COND-1.0",
            "required": True,
        },
    )
