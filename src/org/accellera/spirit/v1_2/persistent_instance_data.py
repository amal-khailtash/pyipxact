from dataclasses import dataclass

from org.accellera.spirit.v1_2.persistent_data_type import PersistentDataType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class PersistentInstanceData(PersistentDataType):
    """A container for any data that is specific to this instance of the design
    object.

    The contents are not interpreted or validated by the Design
    Environment. This element will be saved with the design and restored
    when the design is loaded. It is indended to be used by generators
    to store and retrieve instance specific data.
    """

    class Meta:
        name = "persistentInstanceData"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"
