from collections.abc import Iterable
from dataclasses import dataclass, field

from org.accellera.spirit.v1685_2009.ve.pdp.drive_constraint import (
    DriveConstraint,
)
from org.accellera.spirit.v1685_2009.ve.pdp.load_constraint import (
    LoadConstraint,
)
from org.accellera.spirit.v1685_2009.ve.pdp.timing_constraint import (
    TimingConstraint,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class AbstractionDefPortConstraintsType:
    """
    Defines constraints that apply to a wire type port in an abstraction
    definition.
    """

    class Meta:
        name = "abstractionDefPortConstraintsType"

    timing_constraint: Iterable[TimingConstraint] = field(
        default_factory=list,
        metadata={
            "name": "timingConstraint",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "min_occurs": 1,
        },
    )
    drive_constraint: Iterable[DriveConstraint] = field(
        default_factory=list,
        metadata={
            "name": "driveConstraint",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "max_occurs": 2,
        },
    )
    load_constraint: Iterable[LoadConstraint] = field(
        default_factory=list,
        metadata={
            "name": "loadConstraint",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "max_occurs": 3,
        },
    )
