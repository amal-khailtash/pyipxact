from dataclasses import dataclass, field

from org.accellera.spirit.v1_4.presence_value import PresenceValue

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class Presence:
    """If this element is present, the existance of the port is controlled by the
    specified value.

    valid values are 'illegal', 'required' and 'optional'.
    """

    class Meta:
        name = "presence"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"

    value: PresenceValue = field(default=PresenceValue.OPTIONAL)