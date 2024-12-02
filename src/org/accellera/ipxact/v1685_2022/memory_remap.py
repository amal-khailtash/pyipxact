from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.memory_remap_type import MemoryRemapType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class MemoryRemap(MemoryRemapType):
    """
    Additional memory map elements that are dependent on the component state.
    """

    class Meta:
        name = "memoryRemap"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
