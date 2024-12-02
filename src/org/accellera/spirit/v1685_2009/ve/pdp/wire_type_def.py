from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class WireTypeDef:
    """
    Definition of a single wire type defintion that can relate to multiple views.

    :ivar type_name: The name of the logic type. Examples could be
        std_logic, std_ulogic, std_logic_vector, sc_logic, ...
    :ivar type_definition: Where the definition of the type is
        contained. For std_logic, this is contained in
        IEEE.std_logic_1164.all. For sc_logic, this is contained in
        systemc.h. For VHDL this is the library and package as defined
        by the "used" statement. For SystemC and SystemVerilog it is the
        include file required. For verilog this is not needed.
    :ivar view_name_ref: A reference to a view name in the file for
        which this type applies.
    """

    class Meta:
        name = "wireTypeDef"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    type_name: Optional["WireTypeDef.TypeName"] = field(
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
    view_name_ref: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "viewNameRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class TypeName:
        """
        :ivar value:
        :ivar constrained: Defines that the type for the port has
            constrainted the number of bits in the vector
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
