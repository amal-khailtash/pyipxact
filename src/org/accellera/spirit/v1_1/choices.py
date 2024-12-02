from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class Choices:
    """
    Choices used by user defined properties of spirit:formatType ="choice".

    :ivar choice: Non-empty set of legal values for a user defined
        property of type spirit:formatType="choice" .
    """

    class Meta:
        name = "choices"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    choice: Iterable["Choices.Choice"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class Choice:
        """
        :ivar name: Choice key, available for reference by the
            spirit:choiceRef attribute of user defined properties of
            type spirit:formatType="choice".
        :ivar enumeration: A possible value of spirit:choice
        """

        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        enumeration: Iterable["Choices.Choice.Enumeration"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )

        @dataclass(slots=True)
        class Enumeration:
            """
            :ivar value:
            :ivar text: When specified, displayed in place of the
                spirit:enumeration value
            :ivar help: Text that may be displayed if the user requests
                help about the meaning of an element
            """

            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            text: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            help: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
