from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.core.abstractor_port_type import (
    AbstractorPortType,
)
from org.accellera.spirit.v1685_2009.ve.core.abstractor_view_type import (
    AbstractorViewType,
)
from org.accellera.spirit.v1685_2009.ve.core.name_value_type_type import (
    NameValueTypeType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class AbstractorModelType:
    """
    Model information for an abstractor.

    :ivar views: View container
    :ivar ports: Port container
    :ivar model_parameters: Model parameter name value pairs container
    """

    class Meta:
        name = "abstractorModelType"

    views: Optional["AbstractorModelType.Views"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    ports: Optional["AbstractorModelType.Ports"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )
    model_parameters: Optional["AbstractorModelType.ModelParameters"] = field(
        default=None,
        metadata={
            "name": "modelParameters",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
        },
    )

    @dataclass(slots=True)
    class Views:
        """
        :ivar view: Single view of an abstractor
        """

        view: Iterable[AbstractorViewType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            },
        )

    @dataclass(slots=True)
    class Ports:
        port: Iterable[AbstractorPortType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
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
            Verilog parameter). The usageType attribute indicate how the
            model parameter is to be used.
        """

        model_parameter: Iterable[NameValueTypeType] = field(
            default_factory=list,
            metadata={
                "name": "modelParameter",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            },
        )
