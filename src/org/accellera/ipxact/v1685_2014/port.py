from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.port_type import PortType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Port(PortType):
    """
    Describes port characteristics.
    """

    class Meta:
        name = "port"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
