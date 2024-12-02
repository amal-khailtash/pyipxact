from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.type_parameters import TypeParameters

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class TransTypeDef:
    """
    Definition of a single transactional type defintion.

    :ivar type_name: The name of the port type. Can be any predefined
        type such sc_port or sc_export in SystemC or any user-defined
        type such as tlm_port.
    :ivar type_definition: Where the definition of the type is
        contained. For SystemC and SystemVerilog it is the include file
        containing the type definition.
    :ivar type_parameters:
    :ivar view_ref: A reference to a view name in the file for which
        this type applies.
    :ivar id:
    """

    class Meta:
        name = "transTypeDef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    type_name: Optional["TransTypeDef.TypeName"] = field(
        default=None,
        metadata={
            "name": "typeName",
            "type": "Element",
        },
    )
    type_definition: Iterable["TransTypeDef.TypeDefinition"] = field(
        default_factory=list,
        metadata={
            "name": "typeDefinition",
            "type": "Element",
        },
    )
    type_parameters: Optional[TypeParameters] = field(
        default=None,
        metadata={
            "name": "typeParameters",
            "type": "Element",
        },
    )
    view_ref: Iterable["TransTypeDef.ViewRef"] = field(
        default_factory=list,
        metadata={
            "name": "viewRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass(slots=True)
    class TypeName:
        """
        :ivar value:
        :ivar exact: When false, defines that the type is an abstract
            type that may not be related to an existing type in the
            language of the referenced view.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        exact: bool = field(
            default=True,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(slots=True)
    class TypeDefinition:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

    @dataclass(slots=True)
    class ViewRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )
