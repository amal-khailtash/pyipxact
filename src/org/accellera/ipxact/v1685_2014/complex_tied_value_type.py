from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Optional, Union

from org.accellera.ipxact.v1685_2014.simple_tied_value_type_value import (
    SimpleTiedValueTypeValue,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ComplexTiedValueType:
    """An unsigned longint expression that resolves to the value set {0, 1, ...} or
    open or default.

    It is derived from longintExpression and it supports an expression
    value.

    :ivar value:
    :ivar other_attributes:
    :ivar minimum: For elements which can be specified using expression
        which are supposed to be resolved to a long value, this
        indicates the minimum value allowed.
    :ivar maximum: For elements which can be specified using expression
        which are supposed to be resolved to a long value, this
        indicates the maximum value allowed.
    """

    class Meta:
        name = "complexTiedValueType"

    value: Union[str, SimpleTiedValueTypeValue] = field(
        default="",
        metadata={
            "white_space": "collapse",
        },
    )
    other_attributes: Mapping[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    minimum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maximum: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
