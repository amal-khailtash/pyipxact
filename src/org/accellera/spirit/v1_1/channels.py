from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class Channels:
    """
    Lists all channel connections between mirror interfaces of this component.

    :ivar channel: Defines a set of mirrored interfaces of this
        component that are connected to one another.
    """

    class Meta:
        name = "channels"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    channel: Iterable["Channels.Channel"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class Channel:
        """
        :ivar max_masters: Overrides the maxMasters value in the bus
            definition if this number is more restrictive.
        :ivar max_slaves: Overrides the maxSlaves value in the bus
            definition if this number is more restrictive.
        :ivar bus_interface_ref: Contains the name of one of the bus
            interfaces that is part of this channel.
        """

        max_masters: Optional[int] = field(
            default=None,
            metadata={
                "name": "maxMasters",
                "type": "Element",
            },
        )
        max_slaves: Optional[int] = field(
            default=None,
            metadata={
                "name": "maxSlaves",
                "type": "Element",
            },
        )
        bus_interface_ref: Iterable[str] = field(
            default_factory=list,
            metadata={
                "name": "busInterfaceRef",
                "type": "Element",
            },
        )
