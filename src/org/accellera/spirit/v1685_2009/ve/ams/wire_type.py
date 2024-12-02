from dataclasses import dataclass

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"


@dataclass(slots=True)
class WireType:
    """
    Wire port extension type definition.
    """

    class Meta:
        name = "wireType"
