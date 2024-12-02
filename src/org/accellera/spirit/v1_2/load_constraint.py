from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.capacitance import Capacitance
from org.accellera.spirit.v1_2.cell_specification import CellSpecification

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class LoadConstraint:
    """
    Defines a constraint indicating the type of load on an output signal.

    :ivar cell_specification:
    :ivar count: Indicates how many loads of the specified cell are
        connected. If not present, 3 is assumed.
    :ivar capacitance: Indicates an explicit load capacitance on an
        output signal.
    """

    class Meta:
        name = "loadConstraint"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    cell_specification: Optional[CellSpecification] = field(
        default=None,
        metadata={
            "name": "cellSpecification",
            "type": "Element",
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    capacitance: Optional[Capacitance] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
