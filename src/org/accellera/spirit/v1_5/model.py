from dataclasses import dataclass

from org.accellera.spirit.v1_5.model_type import ModelType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class Model(ModelType):
    """
    Model information.
    """

    class Meta:
        name = "model"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"