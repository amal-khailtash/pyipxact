from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.configurable_arrays import (
    ConfigurableArrays,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Arrays(ConfigurableArrays):
    class Meta:
        name = "arrays"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
