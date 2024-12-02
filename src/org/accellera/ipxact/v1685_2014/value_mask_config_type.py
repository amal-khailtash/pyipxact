from dataclasses import dataclass

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ValueMaskConfigType:
    """
    This type is used to specify a value and optional mask that are configurable.
    """

    class Meta:
        name = "valueMaskConfigType"
