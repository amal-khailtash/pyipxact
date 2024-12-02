from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.initiative_value import InitiativeValue

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class Initiative:
    """
    If this element is present, the type of access is restricted to the specified
    value.
    """

    class Meta:
        name = "initiative"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    value: Optional[InitiativeValue] = field(default=None)
