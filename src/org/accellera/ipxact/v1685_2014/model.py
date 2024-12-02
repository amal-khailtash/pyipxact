from dataclasses import dataclass

from org.accellera.ipxact.v1685_2014.model_type import ModelType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class Model(ModelType):
    """
    Model information.
    """

    class Meta:
        name = "model"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
