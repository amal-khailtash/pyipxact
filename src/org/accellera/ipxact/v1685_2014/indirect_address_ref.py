from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class IndirectAddressRef:
    """
    A reference to a field used for addressing the indirectly accessible memoryMap.
    """

    class Meta:
        name = "indirectAddressRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
