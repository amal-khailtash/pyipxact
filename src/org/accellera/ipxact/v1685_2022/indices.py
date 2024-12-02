from dataclasses import dataclass

from org.accellera.ipxact.v1685_2022.indices_type import IndicesType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class Indices(IndicesType):
    class Meta:
        name = "indices"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
