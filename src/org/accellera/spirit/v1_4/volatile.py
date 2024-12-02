from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class Volatile:
    """
    Indicates whether the data is volatile, default to false when not present.
    """

    class Meta:
        name = "volatile"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )
