from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.power.description import Description
from org.accellera.spirit.v1685_2009.ve.power.display_name import DisplayName
from org.accellera.spirit.v1685_2009.ve.power.hier_interface import (
    HierInterface,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class MonitorInterconnection:
    """Describes a connection from the interface of one component to any number of
    monitor interfaces in the design.

    An active interface can be connected to unlimited number of monitor
    interfaces.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar monitored_active_interface: Describes an active interface of
        the design that all the monitors will be connected to. The
        componentRef and busRef attributes indicate the instance name
        and bus interface name. The optional path attribute indicates
        the hierarchical instance name path to the component.
    :ivar monitor_interface: Describes a list of monitor interfaces that
        are connected to the single active interface. The componentRef
        and busRef attributes indicate the instance name and bus
        interface name. The optional path attribute indicates the
        hierarchical instance name path to the component.
    """

    class Meta:
        name = "monitorInterconnection"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    monitored_active_interface: Optional[HierInterface] = field(
        default=None,
        metadata={
            "name": "monitoredActiveInterface",
            "type": "Element",
            "required": True,
        },
    )
    monitor_interface: Iterable[HierInterface] = field(
        default_factory=list,
        metadata={
            "name": "monitorInterface",
            "type": "Element",
            "min_occurs": 1,
        },
    )
