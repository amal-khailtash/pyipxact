from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.cell_specification import (
    CellSpecification,
)
from org.accellera.ipxact.v1685_2014.unsigned_positive_int_expression import (
    UnsignedPositiveIntExpression,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class LoadConstraint:
    """
    Defines a constraint indicating the type of load on an output port.

    :ivar cell_specification:
    :ivar count: Indicates how many loads of the specified cell are
        connected. If not present, 3 is assumed.
    """

    class Meta:
        name = "loadConstraint"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    cell_specification: Optional[CellSpecification] = field(
        default=None,
        metadata={
            "name": "cellSpecification",
            "type": "Element",
            "required": True,
        },
    )
    count: Optional[UnsignedPositiveIntExpression] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
