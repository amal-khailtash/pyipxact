from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_5.name_value_type_type import NameValueTypeType
from org.accellera.spirit.v1_5.port import Port
from org.accellera.spirit.v1_5.view_type import ViewType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class ModelType:
    """
    Model information.

    :ivar views: View container
    :ivar ports: Port container
    :ivar model_parameters: Model parameter name value pairs container
    """

    class Meta:
        name = "modelType"

    views: Optional["ModelType.Views"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    ports: Optional["ModelType.Ports"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    model_parameters: Optional["ModelType.ModelParameters"] = field(
        default=None,
        metadata={
            "name": "modelParameters",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )

    @dataclass(slots=True)
    class Views:
        """
        :ivar view: Single view of a component
        """

        view: Iterable[ViewType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                "min_occurs": 1,
            },
        )

    @dataclass(slots=True)
    class Ports:
        port: Iterable[Port] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                "min_occurs": 1,
            },
        )

    @dataclass(slots=True)
    class ModelParameters:
        """
        :ivar model_parameter: A model parameter name value pair. The
            name is given in an attribute. The value is the element
            value. The dataType (applicable to high level modeling) is
            given in the dataType attribute. For hardware based models,
            the name should be identical to the RTL (VHDL generic or
            Verilog parameter). The usageType attribute indicates how
            the model parameter is to be used.
        """

        model_parameter: Iterable[NameValueTypeType] = field(
            default_factory=list,
            metadata={
                "name": "modelParameter",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                "min_occurs": 1,
            },
        )
