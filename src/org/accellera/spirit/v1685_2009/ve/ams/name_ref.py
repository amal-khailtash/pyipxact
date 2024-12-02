from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"


@dataclass(slots=True)
class NameRef:
    """
    Reference to an existing spirit name in the file.
    """

    class Meta:
        name = "nameRef"
        namespace = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
