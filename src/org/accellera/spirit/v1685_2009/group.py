from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class Group:
    """Indicates which system interface is being mirrored.

    Name must match a group name present on one or more ports in the
    corresonding bus definition.
    """

    class Meta:
        name = "group"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )