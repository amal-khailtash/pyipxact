from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class Description:
    """
    Full description string, typically for documentation.
    """

    class Meta:
        name = "description"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
