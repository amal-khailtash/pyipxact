from dataclasses import dataclass

from org.accellera.spirit.v1_5.port_type import PortType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class AbstractorPortType(PortType):
    """
    A port description, giving a name and an access type for high level ports.
    """

    class Meta:
        name = "abstractorPortType"
