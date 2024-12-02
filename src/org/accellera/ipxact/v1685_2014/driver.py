from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.driver_type import DriverType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Driver(DriverType):
    """
    Wire port driver element.
    """

    class Meta:
        name = "driver"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
