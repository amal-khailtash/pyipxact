from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_0.add_rem_change_value import AddRemChangeValue

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class AddRemChange:
    """
    Indicates whether the alteration is an addition or a removal.
    """

    class Meta:
        name = "addRemChange"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"

    value: Optional[AddRemChangeValue] = field(default=None)
