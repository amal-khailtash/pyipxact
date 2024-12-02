from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.bus_interface_type import BusInterfaceType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class BusInterface(BusInterfaceType):
    """
    Describes one of the bus interfaces supported by this component.
    """

    class Meta:
        name = "busInterface"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
