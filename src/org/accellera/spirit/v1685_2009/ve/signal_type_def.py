from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.signal_type import SignalType
from org.accellera.spirit.v1685_2009.ve.view_name_ref import ViewNameRef

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/AMS-1.0"
)


@dataclass(slots=True)
class SignalTypeDef:
    """
    Definition of a single signal type definition that can relate to multiple
    views.
    """

    class Meta:
        name = "signalTypeDef"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/AMS-1.0"
        )

    signal_type: Optional[SignalType] = field(
        default=None,
        metadata={
            "name": "signalType",
            "type": "Element",
            "required": True,
        },
    )
    view_name_ref: Iterable[ViewNameRef] = field(
        default_factory=list,
        metadata={
            "name": "viewNameRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE",
            "min_occurs": 1,
        },
    )
