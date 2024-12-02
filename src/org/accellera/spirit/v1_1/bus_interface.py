from dataclasses import dataclass

from org.accellera.spirit.v1_1.bus_interface_type import BusInterfaceType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class BusInterface(BusInterfaceType):
    """
    Describes one of the bus interfaces supported by this component.
    """

    class Meta:
        name = "busInterface"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"
