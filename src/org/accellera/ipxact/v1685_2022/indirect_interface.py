from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.indirect_interface_type import (
    IndirectInterfaceType,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class IndirectInterface(IndirectInterfaceType):
    """
    Describes one of the bus interfaces supported by this component.
    """

    class Meta:
        name = "indirectInterface"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
