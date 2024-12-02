from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.is_present import IsPresent

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class TransparentBridge:
    """If this element is present, it indicates that the bus interface provides a
    transparent bridge to another master bus interface on the same component.

    It has a masterRef attribute which contains the name of the other
    bus interface. Any slave interface can bridge to multiple master
    interfaces, and multiple slave interfaces can bridge to the same
    master interface.

    :ivar is_present:
    :ivar master_ref: The name of the master bus interface to which this
        interface bridges.
    :ivar id:
    """

    class Meta:
        name = "transparentBridge"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    is_present: Optional[IsPresent] = field(
        default=None,
        metadata={
            "name": "isPresent",
            "type": "Element",
        },
    )
    master_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "masterRef",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
