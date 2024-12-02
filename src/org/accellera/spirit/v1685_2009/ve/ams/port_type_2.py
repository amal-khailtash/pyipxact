from dataclasses import dataclass

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/SPIRIT/1685-2009-VE"


@dataclass(slots=True)
class PortType2:
    """
    Port extension type definition.
    """

    class Meta:
        name = "portType"
