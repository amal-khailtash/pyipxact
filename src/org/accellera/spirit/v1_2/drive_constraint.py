from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.cell_specification import CellSpecification
from org.accellera.spirit.v1_2.resistance import Resistance

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class DriveConstraint:
    """Defines a constraint indicating how an input is to be driven.

    The preferred methodology is to specify a library cell in technology
    independent fashion. The implemention tool should assume that the
    associated signal is driven by the specified cell, or that the drive
    strength of the input signal is indicated by the specified
    resistance value.

    :ivar cell_specification:
    :ivar resistance: Specifes a drive resistance for the input signal.
    """

    class Meta:
        name = "driveConstraint"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    cell_specification: Optional[CellSpecification] = field(
        default=None,
        metadata={
            "name": "cellSpecification",
            "type": "Element",
        },
    )
    resistance: Optional[Resistance] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
