from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_0.add_rem_rep_change_value import (
    AddRemRepChangeValue,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class AddRemRepChange:
    """
    Indicates whether the alteration is an addition, removal or a replacement.
    """

    class Meta:
        name = "addRemRepChange"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"

    value: Optional[AddRemRepChangeValue] = field(default=None)
