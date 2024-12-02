from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class Dependency:
    """Specifies a location on which  files or fileSets may be dependent.

    Typically, this would be a directory that would contain included
    files.
    """

    class Meta:
        name = "dependency"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
