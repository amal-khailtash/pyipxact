from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_4.interface import Interface

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class MonitorInterconnection:
    """Describes a connection from the interface of one component to any number of
    monitor interfaces in the design.

    An active interface can be connected to unlimited number of monitor
    interfaces.

    :ivar name: Unique name
    :ivar display_name: Element name for display purposes. Typically a
        few words providing a more detailed and/or user-friendly name
        than the spirit:name.
    :ivar description: Full description string, typically for
        documentation
    :ivar active_interface: Describes an active interface of the design
        that all the monitors will be connected to. The componentRef and
        busRef attributes indicate the instance name and bus interface
        name.
    :ivar monitor_interface: Describes a list of monitor interfaces that
        are connected to the single active interface. The componentRef
        and busRef attributes indicate the instance name and bus
        interface name.
    """

    class Meta:
        name = "monitorInterconnection"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    active_interface: Optional[Interface] = field(
        default=None,
        metadata={
            "name": "activeInterface",
            "type": "Element",
            "required": True,
        },
    )
    monitor_interface: Iterable[Interface] = field(
        default_factory=list,
        metadata={
            "name": "monitorInterface",
            "type": "Element",
            "min_occurs": 1,
        },
    )
