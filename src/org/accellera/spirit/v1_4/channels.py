from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class Channels:
    """
    Lists all channel connections between mirror interfaces of this component.

    :ivar channel: Defines a set of mirrored interfaces of this
        component that are connected to one another.
    """

    class Meta:
        name = "channels"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"

    channel: Iterable["Channels.Channel"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class Channel:
        """
        :ivar name: Unique name
        :ivar display_name: Element name for display purposes. Typically
            a few words providing a more detailed and/or user-friendly
            name than the spirit:name.
        :ivar description: Full description string, typically for
            documentation
        :ivar bus_interface_ref: Contains the name of one of the bus
            interfaces that is part of this channel. The ordering of the
            references may be important to the design environment.
        """

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
        bus_interface_ref: Iterable[str] = field(
            default_factory=list,
            metadata={
                "name": "busInterfaceRef",
                "type": "Element",
                "min_occurs": 2,
            },
        )
