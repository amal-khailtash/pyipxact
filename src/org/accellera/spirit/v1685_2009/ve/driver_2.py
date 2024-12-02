from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1685_2009.ve.view_name_ref import ViewNameRef

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/CORE-1.0"
)


@dataclass(slots=True)
class Driver2:
    """
    Wire port driver extension.

    :ivar default_value: Default value for a wire port extension. Type
        is a list of float. The list elements match with the port vector
        elements from left to right.
    :ivar view_name_ref:
    """

    class Meta:
        name = "driver"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/CORE-1.0"
        )

    default_value: Iterable[float] = field(
        default_factory=list,
        metadata={
            "name": "defaultValue",
            "type": "Element",
            "tokens": True,
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
