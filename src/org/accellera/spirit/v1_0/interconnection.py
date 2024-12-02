from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class Interconnection:
    """Describes a connection from the interace of one comonent to the interface of
    another component through its attributes.

    The component1Ref and busInterface1Ref attributes indicate the
    instance name and bus interface name of one end of the connection.
    The component2Ref and busInterface2Ref attributes indicate the
    instance name and bus interface name of the other end of he
    connection.
    """

    class Meta:
        name = "interconnection"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"

    component1_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "component1Ref",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
    bus_interface1_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "busInterface1Ref",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
    component2_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "component2Ref",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
    bus_interface2_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "busInterface2Ref",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
