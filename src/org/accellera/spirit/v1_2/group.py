from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class Group:
    """Indicates which system interface is being mirrored.

    Name must match a group name present on one or more signals in the
    corresonding bus definition.
    """

    class Meta:
        name = "group"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
