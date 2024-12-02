from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.cell_specification import (
    CellSpecification,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class DriveConstraint:
    """Defines a constraint indicating how an input is to be driven.

    The preferred methodology is to specify a library cell in technology
    independent fashion. The implemention tool should assume that the
    associated port is driven by the specified cell, or that the drive
    strength of the input port is indicated by the specified resistance
    value.
    """

    class Meta:
        name = "driveConstraint"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    cell_specification: Optional[CellSpecification] = field(
        default=None,
        metadata={
            "name": "cellSpecification",
            "type": "Element",
            "required": True,
        },
    )
