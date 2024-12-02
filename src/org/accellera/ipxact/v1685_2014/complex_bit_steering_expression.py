from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Union

from org.accellera.ipxact.v1685_2014.simple_bit_steering_expression_value import (
    SimpleBitSteeringExpressionValue,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ComplexBitSteeringExpression:
    """Indicates whether bit steering should be used to map this interface onto a
    bus of different data width.

    Values are "on", "off" or an expression which resolves to an
    unsigned-bit where a '1' indicates "on" and a '0' indicates "off"
    (defaults to "off").
    """

    class Meta:
        name = "complexBitSteeringExpression"

    value: Union[str, SimpleBitSteeringExpressionValue] = field(
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
