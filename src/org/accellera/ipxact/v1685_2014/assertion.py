from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.description import Description
from org.accellera.ipxact.v1685_2014.display_name import DisplayName
from org.accellera.ipxact.v1685_2014.unsigned_bit_expression import (
    UnsignedBitExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Assertion:
    """Provides an expression for describing valid parameter value settings.

    If a assertion assert expression evaluates false, the name,
    displayName and/or description can be used to communicate the
    assertion failure.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar assert_value:
    :ivar id:
    """

    class Meta:
        name = "assertion"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

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
    assert_value: Optional[UnsignedBitExpression] = field(
        default=None,
        metadata={
            "name": "assert",
            "type": "Element",
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
