from dataclasses import dataclass, field

from org.accellera.ipxact.v1685_2014.presence_type import PresenceType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Presence:
    """If this element is present, the existance of the port is controlled by the
    specified value.

    valid values are 'illegal', 'required' and 'optional'.
    """

    class Meta:
        name = "presence"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    value: PresenceType = field(
        default=PresenceType.OPTIONAL,
        metadata={
            "required": True,
        },
    )
