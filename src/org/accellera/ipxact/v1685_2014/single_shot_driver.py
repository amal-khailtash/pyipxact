from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.real_expression import RealExpression
from org.accellera.ipxact.v1685_2014.unsigned_bit_vector_expression import (
    UnsignedBitVectorExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class SingleShotDriver:
    """
    Describes a driven one-shot port.

    :ivar single_shot_offset: Time in nanoseconds until start of one-
        shot.
    :ivar single_shot_value: Value of port after first  edge of one-
        shot.
    :ivar single_shot_duration: Duration in nanoseconds of the one shot.
    """

    class Meta:
        name = "singleShotDriver"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    single_shot_offset: Optional[RealExpression] = field(
        default=None,
        metadata={
            "name": "singleShotOffset",
            "type": "Element",
            "required": True,
        },
    )
    single_shot_value: Optional[UnsignedBitVectorExpression] = field(
        default=None,
        metadata={
            "name": "singleShotValue",
            "type": "Element",
            "required": True,
        },
    )
    single_shot_duration: Optional[RealExpression] = field(
        default=None,
        metadata={
            "name": "singleShotDuration",
            "type": "Element",
            "required": True,
        },
    )
