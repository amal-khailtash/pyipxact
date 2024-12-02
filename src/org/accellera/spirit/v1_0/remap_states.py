from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class RemapStates:
    """
    Contains a list of remap state names and associated signal values.

    :ivar remap_state: Contains a list of signals and values which tell
        the decoder to enter this remap state. The name attribute
        identifies the name of the state
    """

    class Meta:
        name = "remapStates"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"

    remap_state: Iterable["RemapStates.RemapState"] = field(
        default_factory=list,
        metadata={
            "name": "remapState",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class RemapState:
        """
        :ivar remap_signal: Contains the name and value of a signal on
            the component, the value indicates the logic value which
            this signal must take to effect the remapping. The id
            attribute stores the name of the signal which takes that
            value.
        :ivar name: Stores the name of the state
        """

        remap_signal: Iterable["RemapStates.RemapState.RemapSignal"] = field(
            default_factory=list,
            metadata={
                "name": "remapSignal",
                "type": "Element",
                "min_occurs": 1,
            },
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                "required": True,
            },
        )

        @dataclass(slots=True)
        class RemapSignal:
            """
            :ivar value:
            :ivar id: This attribute identifies a signal on the
                component which affects the component's memory layout
            """

            value: Optional[bool] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
                    "required": True,
                },
            )
