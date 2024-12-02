from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class BitsInLau:
    """The number of bits in the least addressable unit.

    The default is byte addressable (8 bits).
    """

    class Meta:
        name = "bitsInLau"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
