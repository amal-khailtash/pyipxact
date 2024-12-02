from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.power.access_type import AccessType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


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
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    value: Optional[AccessType] = field(default=None)
