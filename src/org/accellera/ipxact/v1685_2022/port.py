from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.port_type import PortType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Port(PortType):
    """
    Describes port characteristics.
    """

    class Meta:
        name = "port"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
