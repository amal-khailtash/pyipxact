from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class Interface:
    """
    A representation of a component/bus interface relation; i.e. a bus interface
    belonging to a certain component.

    :ivar component_ref: Reference to a component instance name.
    :ivar bus_ref: Reference to the components  bus interface
    """

    class Meta:
        name = "interface"

    component_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "componentRef",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            "required": True,
        },
    )
    bus_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "busRef",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            "required": True,
        },
    )
