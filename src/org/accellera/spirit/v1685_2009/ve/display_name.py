from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class DisplayName:
    """Element name for display purposes.

    Typically a few words providing a more detailed and/or user-friendly
    name than the spirit:name.
    """

    class Meta:
        name = "displayName"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
