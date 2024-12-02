from dataclasses import dataclass

from org.accellera.spirit.v1685_2009.ve.ams.port_type_1 import PortType1

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class Port1(PortType1):
    """
    Describes port characteristics.
    """

    class Meta:
        name = "port"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )
