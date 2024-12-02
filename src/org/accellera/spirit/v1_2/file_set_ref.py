from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class FileSetRef:
    """
    A reference to a fileSet.
    """

    class Meta:
        name = "fileSetRef"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
