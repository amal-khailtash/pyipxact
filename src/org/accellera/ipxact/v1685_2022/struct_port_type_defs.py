from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2022.type_parameter import TypeParameter

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(slots=True)
class StructPortTypeDefs:
    class Meta:
        name = "structPortTypeDefs"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    struct_port_type_def: Iterable["StructPortTypeDefs.StructPortTypeDef"] = (
        field(
            default_factory=list,
            metadata={
                "name": "structPortTypeDef",
                "type": "Element",
                "min_occurs": 1,
            },
        )
    )

    @dataclass(slots=True)
    class StructPortTypeDef:
        """
        :ivar type_name:
        :ivar type_definition: Where the definition of the type is
            contained. For SystemC and SystemVerilog it is the include
            file containing the type definition.
        :ivar type_parameters:
        :ivar role: Indicates the role that this structured port plays
            in the connection.  Only valid for structured ports with
            structType='interface'. In SystemVerilog, this indicates the
            modport for the SystemVerilog interface corresponding to
            this structuredPortType.
        :ivar view_ref: A reference to a view name in the file for which
            this type applies.
        :ivar id:
        """

        type_name: Optional[
            "StructPortTypeDefs.StructPortTypeDef.TypeName"
        ] = field(
            default=None,
            metadata={
                "name": "typeName",
                "type": "Element",
                "required": True,
            },
        )
        type_definition: Iterable[
            "StructPortTypeDefs.StructPortTypeDef.TypeDefinition"
        ] = field(
            default_factory=list,
            metadata={
                "name": "typeDefinition",
                "type": "Element",
            },
        )
        type_parameters: Optional[
            "StructPortTypeDefs.StructPortTypeDef.TypeParameters"
        ] = field(
            default=None,
            metadata={
                "name": "typeParameters",
                "type": "Element",
            },
        )
        role: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        view_ref: Iterable["StructPortTypeDefs.StructPortTypeDef.ViewRef"] = (
            field(
                default_factory=list,
                metadata={
                    "name": "viewRef",
                    "type": "Element",
                },
            )
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
            :ivar constrained: Defines the types for the port has
                constrained the number of bits in the vector
            """

            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            constrained: Iterable[str] = field(
                default_factory=list,
                metadata={
                    "type": "Attribute",
                    "tokens": True,
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
        class TypeParameters:
            type_parameter: Iterable[TypeParameter] = field(
                default_factory=list,
                metadata={
                    "name": "typeParameter",
                    "type": "Element",
                    "min_occurs": 1,
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