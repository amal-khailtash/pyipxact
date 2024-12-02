from dataclasses import dataclass

from org.accellera.spirit.v1685_2009.ve.power.port_type_1 import PortType1

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class AbstractorPortType(PortType1):
    """
    A port description, giving a name and an access type for high level ports.
    """

    class Meta:
        name = "abstractorPortType"
