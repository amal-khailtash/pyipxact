from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class PortAccessHandle:
    """If present, is a method to be used to get hold of the object representing
    the port.

    This is typically a function call or array element reference in
    systemC.
    """

    class Meta:
        name = "portAccessHandle"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
