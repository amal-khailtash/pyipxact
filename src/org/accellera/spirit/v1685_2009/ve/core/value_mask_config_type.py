from dataclasses import dataclass

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class ValueMaskConfigType:
    """
    This type is used to specify a value and optional mask that are configurable.
    """

    class Meta:
        name = "valueMaskConfigType"
