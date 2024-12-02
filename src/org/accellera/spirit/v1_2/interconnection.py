from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.interface import Interface

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class Interconnection:
    """Describes a connection from the interface of one component to the interface
    of another component through its attributes.

    The componentRef and busInterfaceRef attributes indicate the
    instance name and bus interface name of one end of the connection.
    The interconnection element connects two active interfaces and
    doesn't connect monitor interfaces.

    :ivar name: name of the connection
    :ivar active_interface:
    """

    class Meta:
        name = "interconnection"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    active_interface: Iterable[Interface] = field(
        default_factory=list,
        metadata={
            "name": "activeInterface",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
