from dataclasses import dataclass

from org.accellera.spirit.v1685_2009.port_type import PortType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class Port(PortType):
    """
    Describes port characteristics.
    """

    class Meta:
        name = "port"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )
