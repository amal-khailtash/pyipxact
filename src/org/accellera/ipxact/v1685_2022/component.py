from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.component_type import ComponentType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Component(ComponentType):
    """
    This is the root element for all non platform-core components.
    """

    class Meta:
        name = "component"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
