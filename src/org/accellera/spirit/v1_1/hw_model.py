from dataclasses import dataclass

from org.accellera.spirit.v1_1.hw_model_type import HwModelType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class HwModel(HwModelType):
    """
    Hardware model information.
    """

    class Meta:
        name = "hwModel"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"
