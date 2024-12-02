from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.capacitance import Capacitance
from org.accellera.spirit.v1_1.delay import Delay

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class DesignRuleConstraints:
    """
    Defines signal and/or component constraints associated with circuit design
    rules.

    :ivar min_cap: Minimum capacitance value for this component or
        signal. The units attribute can be used to indicate the units
        associated with the capacitance value. Default unit value is
        'pf'.
    :ivar max_cap: Maximum capacitance value for this component or
        signal.
    :ivar min_transition: Minimum transition delay for this component or
        signal.
    :ivar max_transition: Maximum transition delay for this component or
        signal.
    :ivar max_fanout: Maximum fanout value for this component or signal.
    """

    class Meta:
        name = "designRuleConstraints"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    min_cap: Optional[Capacitance] = field(
        default=None,
        metadata={
            "name": "minCap",
            "type": "Element",
        },
    )
    max_cap: Optional[Capacitance] = field(
        default=None,
        metadata={
            "name": "maxCap",
            "type": "Element",
        },
    )
    min_transition: Optional["DesignRuleConstraints.MinTransition"] = field(
        default=None,
        metadata={
            "name": "minTransition",
            "type": "Element",
        },
    )
    max_transition: Optional["DesignRuleConstraints.MaxTransition"] = field(
        default=None,
        metadata={
            "name": "maxTransition",
            "type": "Element",
        },
    )
    max_fanout: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxFanout",
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class MinTransition:
        """
        :ivar rise_delay: Minimum transition delay for a rising edge
            transition for this component or signal.
        :ivar fall_delay: Minimum transition delay for a falling edge
            transition for this component or signal.
        """

        rise_delay: Optional[Delay] = field(
            default=None,
            metadata={
                "name": "riseDelay",
                "type": "Element",
            },
        )
        fall_delay: Optional[Delay] = field(
            default=None,
            metadata={
                "name": "fallDelay",
                "type": "Element",
            },
        )

    @dataclass(slots=True)
    class MaxTransition:
        """
        :ivar rise_delay: Maximum transition delay for a rising edge
            transition for this component or signal.
        :ivar fall_delay: Maximum transition delay for a falling edge
            transition for this component or signal.
        """

        rise_delay: Optional[Delay] = field(
            default=None,
            metadata={
                "name": "riseDelay",
                "type": "Element",
            },
        )
        fall_delay: Optional[Delay] = field(
            default=None,
            metadata={
                "name": "fallDelay",
                "type": "Element",
            },
        )
