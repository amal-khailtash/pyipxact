from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1_2.bus_interface import BusInterface

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class BusInterfaces:
    """
    A list of bus interfaces supported by this component.
    """

    class Meta:
        name = "busInterfaces"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    bus_interface: Iterable[BusInterface] = field(
        default_factory=list,
        metadata={
            "name": "busInterface",
            "type": "Element",
        },
    )