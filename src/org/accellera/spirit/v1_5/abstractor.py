from dataclasses import dataclass

from org.accellera.spirit.v1_5.abstractor_type import AbstractorType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class Abstractor(AbstractorType):
    """
    This is the root element for abstractors.
    """

    class Meta:
        name = "abstractor"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"
