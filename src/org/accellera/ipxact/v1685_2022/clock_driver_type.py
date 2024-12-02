from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.delay_value_unit_type import (
    DelayValueUnitType,
)
from org.accellera.ipxact.v1685_2022.real_expression import RealExpression
from org.accellera.ipxact.v1685_2022.unsigned_bit_expression import (
    UnsignedBitExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class ClockDriverType:
    """
    :ivar clock_period: Clock period in units defined by the units
        attribute. Default is nanoseconds.
    :ivar clock_pulse_offset: Time until first pulse. Units are defined
        by the units attribute. Default is nanoseconds.
    :ivar clock_pulse_value: Value of port after first clock edge.
    :ivar clock_pulse_duration: Duration of first state in cycle. Units
        are defined by the units attribute. Default is nanoseconds.
    :ivar id:
    """

    class Meta:
        name = "clockDriverType"

    clock_period: Optional["ClockDriverType.ClockPeriod"] = field(
        default=None,
        metadata={
            "name": "clockPeriod",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    clock_pulse_offset: Optional["ClockDriverType.ClockPulseOffset"] = field(
        default=None,
        metadata={
            "name": "clockPulseOffset",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    clock_pulse_value: Optional[UnsignedBitExpression] = field(
        default=None,
        metadata={
            "name": "clockPulseValue",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    clock_pulse_duration: Optional["ClockDriverType.ClockPulseDuration"] = (
        field(
            default=None,
            metadata={
                "name": "clockPulseDuration",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "required": True,
            },
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass(slots=True)
    class ClockPeriod(RealExpression):
        units: DelayValueUnitType = field(
            default=DelayValueUnitType.NS,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(slots=True)
    class ClockPulseOffset(RealExpression):
        units: DelayValueUnitType = field(
            default=DelayValueUnitType.NS,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(slots=True)
    class ClockPulseDuration(RealExpression):
        units: DelayValueUnitType = field(
            default=DelayValueUnitType.NS,
            metadata={
                "type": "Attribute",
            },
        )
