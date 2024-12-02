from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Description:
    """
    Full description string, typically for documentation.
    """

    class Meta:
        name = "description"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
