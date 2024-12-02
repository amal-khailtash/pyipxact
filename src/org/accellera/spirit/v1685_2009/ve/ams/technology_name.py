from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.ams.type_value import TypeValue

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0"
)


@dataclass(slots=True)
class TechnologyName:
    """
    Technology name.
    """

    class Meta:
        name = "technologyName"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: Optional[TypeValue] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0",
        },
    )
