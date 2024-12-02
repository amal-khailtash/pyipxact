from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.core.parameter import Parameter

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class ServiceTypeDef:
    """
    Definition of a single service type defintion.

    :ivar type_name: The name of the service type. Can be any predefined
        type such as booean or integer or any user-defined type such as
        addr_type or data_type.
    :ivar type_definition: Where the definition of the type is contained
        if the type if not part of the language. For SystemC and
        SystemVerilog it is the include file containing the type
        definition.
    :ivar parameters: list service parameters (e.g. parameters for a
        systemVerilog interface)
    """

    class Meta:
        name = "serviceTypeDef"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    type_name: Optional["ServiceTypeDef.TypeName"] = field(
        default=None,
        metadata={
            "name": "typeName",
            "type": "Element",
            "required": True,
        },
    )
    type_definition: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "typeDefinition",
            "type": "Element",
        },
    )
    parameters: Optional["ServiceTypeDef.Parameters"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class TypeName:
        """
        :ivar value:
        :ivar constrained: Defines that the type for the port has
            constrainted the number of bits in the vector
        :ivar implicit: Defines that the typeName supplied for this
            service is implicit and a netlister should not declare this
            service in a language specific top-level netlist
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        constrained: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            },
        )
        implicit: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            },
        )

    @dataclass(slots=True)
    class Parameters:
        parameter: Iterable[Parameter] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            },
        )
