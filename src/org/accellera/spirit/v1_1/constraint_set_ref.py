from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class ConstraintSetRef:
    """
    A reference to a set of constraints (signalConstraints, componentConstraints,
    or busDefConstraints).
    """

    class Meta:
        name = "constraintSetRef"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
