from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1685_2009.ve.power.combinational_path_def import (
    CombinationalPathDef,
)

__NAMESPACE__ = (
    "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0"
)


@dataclass(slots=True)
class CombinationalPaths:
    """
    A list of combinational paths crossing the component by means of output ports
    (sink) directly dependent on input ports (sources).
    """

    class Meta:
        name = "combinationalPaths"
        namespace = (
            "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE/PDP-1.0"
        )

    combinational_path: Iterable[CombinationalPathDef] = field(
        default_factory=list,
        metadata={
            "name": "combinationalPath",
            "type": "Element",
            "min_occurs": 1,
        },
    )
