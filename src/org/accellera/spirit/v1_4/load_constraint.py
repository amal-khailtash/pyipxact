from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_4.cell_specification import CellSpecification

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


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
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"

    cell_specification: Optional[CellSpecification] = field(
        default=None,
        metadata={
            "name": "cellSpecification",
            "type": "Element",
            "required": True,
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
