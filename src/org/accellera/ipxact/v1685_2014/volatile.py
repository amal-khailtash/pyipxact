from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Volatile:
    """
    Indicates whether the data is volatile.
    """

    class Meta:
        name = "volatile"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )
