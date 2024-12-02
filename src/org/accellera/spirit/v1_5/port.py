from dataclasses import dataclass

from org.accellera.spirit.v1_5.port_type import PortType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class Port(PortType):
    """
    Describes port characteristics.
    """

    class Meta:
        name = "port"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"
