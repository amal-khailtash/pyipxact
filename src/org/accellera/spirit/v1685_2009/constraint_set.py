from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.description import Description
from org.accellera.spirit.v1685_2009.display_name import DisplayName
from org.accellera.spirit.v1685_2009.drive_constraint import DriveConstraint
from org.accellera.spirit.v1685_2009.load_constraint import LoadConstraint
from org.accellera.spirit.v1685_2009.timing_constraint import TimingConstraint

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class ConstraintSet:
    """Defines constraints that apply to a component port.

    If multiple constraintSet elements are used, each must have a unique
    value for the constraintSetId attribute.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar vector: The optional element vector specify the bits of a
        vector for which the constraints apply. The vaules of left and
        right must be within the range of the port. If the vector is not
        specified then the constraints apply to all the bits of the
        port.
    :ivar drive_constraint:
    :ivar load_constraint:
    :ivar timing_constraint:
    :ivar constraint_set_id:
    """

    class Meta:
        name = "constraintSet"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vector: Optional["ConstraintSet.Vector"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    drive_constraint: Optional[DriveConstraint] = field(
        default=None,
        metadata={
            "name": "driveConstraint",
            "type": "Element",
        },
    )
    load_constraint: Optional[LoadConstraint] = field(
        default=None,
        metadata={
            "name": "loadConstraint",
            "type": "Element",
        },
    )
    timing_constraint: Iterable[TimingConstraint] = field(
        default_factory=list,
        metadata={
            "name": "timingConstraint",
            "type": "Element",
        },
    )
    constraint_set_id: str = field(
        default="default",
        metadata={
            "name": "constraintSetId",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )

    @dataclass(slots=True)
    class Vector:
        """
        :ivar left: The optional elements left and right can be used to
            select a bit-slice of a vector.
        :ivar right: The optional elements left and right can be used to
            select a bit-slice of a vector.
        """

        left: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        right: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
