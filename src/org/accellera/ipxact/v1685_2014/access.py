from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.access_type import AccessType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Access:
    """Indicates the accessibility of the data in the address bank, address block,
    register or field.

    Possible values are 'read-write', 'read-only',  'write-only',
    'writeOnce' and 'read-writeOnce'. If not specified the value is
    inherited from the containing object.
    """

    class Meta:
        name = "access"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    value: Optional[AccessType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
