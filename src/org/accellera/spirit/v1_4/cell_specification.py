from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_4.cell_class_value_type import CellClassValueType
from org.accellera.spirit.v1_4.cell_function_value_type import (
    CellFunctionValueType,
)
from org.accellera.spirit.v1_4.cell_strength_value_type import (
    CellStrengthValueType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class CellSpecification:
    """
    Used to provide a generic description of a technology library cell.

    :ivar cell_function: Defines a technology library cell in library
        independent fashion, based on specification of a cell function
        and strength.
    :ivar cell_class: Defines a technology library cell in library
        independent fashion, based on specification of a cell class and
        strength.
    """

    class Meta:
        name = "cellSpecification"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"

    cell_function: Optional["CellSpecification.CellFunction"] = field(
        default=None,
        metadata={
            "name": "cellFunction",
            "type": "Element",
        },
    )
    cell_class: Optional["CellSpecification.CellClass"] = field(
        default=None,
        metadata={
            "name": "cellClass",
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class CellFunction:
        value: Optional[CellFunctionValueType] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        cell_strength: Optional[CellStrengthValueType] = field(
            default=None,
            metadata={
                "name": "cellStrength",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            },
        )

    @dataclass(slots=True)
    class CellClass:
        value: Optional[CellClassValueType] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        cell_strength: Optional[CellStrengthValueType] = field(
            default=None,
            metadata={
                "name": "cellStrength",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4",
            },
        )
