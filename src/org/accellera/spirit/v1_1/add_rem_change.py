from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.add_rem_change_value import AddRemChangeValue

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class AddRemChange:
    """
    Indicates whether the alteration is an addition or a removal.
    """

    class Meta:
        name = "addRemChange"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    value: Optional[AddRemChangeValue] = field(default=None)
