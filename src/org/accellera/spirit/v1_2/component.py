from dataclasses import dataclass

from org.accellera.spirit.v1_2.component_type import ComponentType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class Component(ComponentType):
    """
    This is the root element for all non platform-core components.
    """

    class Meta:
        name = "component"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"