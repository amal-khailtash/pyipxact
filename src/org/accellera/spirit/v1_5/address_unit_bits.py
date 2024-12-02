from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class AddressUnitBits:
    """The number of data bits in an addressable unit.

    The default is byte addressable (8 bits).
    """

    class Meta:
        name = "addressUnitBits"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
