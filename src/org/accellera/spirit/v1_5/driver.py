from dataclasses import dataclass

from org.accellera.spirit.v1_5.driver_type import DriverType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class Driver(DriverType):
    """
    Wire port driver element.
    """

    class Meta:
        name = "driver"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"
