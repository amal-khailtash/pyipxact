from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.complex_base_expression import (
    ComplexBaseExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Choices:
    """
    Choices used by elements with an attribute ipxact:choiceRef.

    :ivar choice: Non-empty set of legal values for a elements with an
        attribute ipxact:choiceRef.
    """

    class Meta:
        name = "choices"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

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
            ipxact:choiceRef attribute.
        :ivar enumeration: One possible value of ipxact:choice
        :ivar id:
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
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

        @dataclass(slots=True)
        class Enumeration(ComplexBaseExpression):
            """
            :ivar text: When specified, displayed in place of the
                ipxact:enumeration value
            :ivar help: Text that may be displayed if the user requests
                help about the meaning of an element
            :ivar id:
            """

            text: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )
            help: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.w3.org/XML/1998/namespace",
                },
            )