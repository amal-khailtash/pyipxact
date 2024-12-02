from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_5.constraint_set_ref import ConstraintSetRef
from org.accellera.spirit.v1_5.description import Description
from org.accellera.spirit.v1_5.display_name import DisplayName
from org.accellera.spirit.v1_5.file_builder_type import FileBuilderType
from org.accellera.spirit.v1_5.file_set_ref import FileSetRef
from org.accellera.spirit.v1_5.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_5.parameters import Parameters
from org.accellera.spirit.v1_5.vendor_extensions import VendorExtensions
from org.accellera.spirit.v1_5.whitebox_element_ref_type import (
    WhiteboxElementRefType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class ViewType:
    """
    Component view type.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar env_identifier: Defines the hardware environment in which this
        view applies. The format of the string is
        language:tool:vendor_extension, with each piece being optional.
        The language must be one of the types from spirit:fileType. The
        tool values are defined by the SPIRIT Consortium, and include
        generic values "*Simulation" and "*Synthesis" to imply any tool
        of the indicated type. Having more than one envIdentifier
        indicates that the view applies to multiple environments.
    :ivar hierarchy_ref: References an IP-XACT design or configuration
        document (by VLNV) that provides a design for the component
    :ivar language: The hardware description language used such as
        "verilog" or "vhdl". If the attribute "strict" is "true", this
        value must match the language being generated for the design.
    :ivar model_name: Language specific name to identity the model.
        Verilog or SystemVerilog this is the module name. For VHDL this
        is, with ()’s, the entity(architecture) name pair or without, a
        single configuration name.  For SystemC this is the class name.
    :ivar default_file_builder: Default command and flags used to build
        derived files from the sourceName files in the referenced file
        sets.
    :ivar file_set_ref:
    :ivar constraint_set_ref:
    :ivar whitebox_element_refs: Container for white box element
        references.
    :ivar parameters:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "viewType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    env_identifier: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "envIdentifier",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "min_occurs": 1,
            "pattern": r"[a-zA-Z0-9_+\*\.]*:[a-zA-Z0-9_+\*\.]*:[a-zA-Z0-9_+\*\.]*",
        },
    )
    hierarchy_ref: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "name": "hierarchyRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    language: Optional["ViewType.Language"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    model_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelName",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    default_file_builder: Iterable[FileBuilderType] = field(
        default_factory=list,
        metadata={
            "name": "defaultFileBuilder",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    file_set_ref: Iterable[FileSetRef] = field(
        default_factory=list,
        metadata={
            "name": "fileSetRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    constraint_set_ref: Iterable[ConstraintSetRef] = field(
        default_factory=list,
        metadata={
            "name": "constraintSetRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    whitebox_element_refs: Optional["ViewType.WhiteboxElementRefs"] = field(
        default=None,
        metadata={
            "name": "whiteboxElementRefs",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
        },
    )

    @dataclass(slots=True)
    class Language:
        """
        :ivar value:
        :ivar strict: A value of 'true' indicates that this value must
            match the language being generated for the design.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        strict: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )

    @dataclass(slots=True)
    class WhiteboxElementRefs:
        """
        :ivar whitebox_element_ref: Reference to a white box element
            which is visible within this view.
        """

        whitebox_element_ref: Iterable[WhiteboxElementRefType] = field(
            default_factory=list,
            metadata={
                "name": "whiteboxElementRef",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            },
        )
