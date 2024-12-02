from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class ConstraintSetRef:
    """
    A reference to a set of port constraints.
    """

    class Meta:
        name = "constraintSetRef"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
