from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.strength import Strength
from org.accellera.spirit.v1_2.value import Value

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class SignalValueType:
    """Describes a signal value.

    The signal value can be just a value (number), a strength, or both.
    If the "value" is not given, it should be considered an X (unknown).
    A weak strength with no value given is considered Z (tristate).
    """

    class Meta:
        name = "signalValueType"

    strength: Iterable[Strength] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "max_occurs": 2,
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
