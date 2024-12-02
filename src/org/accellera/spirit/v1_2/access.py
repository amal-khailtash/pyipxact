from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.access_type import AccessType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class Access:
    """Indicates the accessibility of the data in the address block.

    Possible values are 'read-write', 'read-only' and 'write-only'.
    """

    class Meta:
        name = "access"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    value: Optional[AccessType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
