from dataclasses import dataclass

from org.accellera.spirit.v1685_2009.ve.power.component_type_1 import (
    ComponentType1,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class Component1(ComponentType1):
    """
    This is the root element for all non platform-core components.
    """

    class Meta:
        name = "component"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )
