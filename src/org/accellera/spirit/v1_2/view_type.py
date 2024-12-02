from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.constraint_set_ref import ConstraintSetRef
from org.accellera.spirit.v1_2.file_builder_type import FileBuilderType
from org.accellera.spirit.v1_2.file_set_ref import FileSetRef
from org.accellera.spirit.v1_2.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_2.parameter import Parameter
from org.accellera.spirit.v1_2.vendor_extensions import VendorExtensions
from org.accellera.spirit.v1_2.whitebox_element_ref_type import (
    WhiteboxElementRefType,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class ViewType:
    """
    :ivar name: Name of the view. Must be unique within a component.
    :ivar env_identifier: Defines the hardware environment in which this
        view applies. The format of the string is
        language:tool:vendor_extension, with each piece being optional.
        The language must be one of the types from spirit:fileType. The
        tool values are defined by the SPIRIT Consortium, and include
        generic values "*Simulation" and "*Synthesis" to imply any tool
        of the indicated type. Having more than one envIdentifier
        indicates that the view applies to multiple environments.
    :ivar hierarchy_ref: References a SPIRIT design or configuration
        document (by VLNV) that provides a design for the component
    :ivar language: The hardware description language used such as
        "verilog" or "vhdl". If the attribute "strict" is "true", this
        value must match the language being generated for the design.
    :ivar model_name: HDL-specific name to identify the model.
    :ivar default_file_builder:
    :ivar file_set_ref:
    :ivar constraint_set_ref:
    :ivar whitebox_element_refs: Container for white box element
        references.
    :ivar parameter:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "viewType"

    name: str = field(
        default="default",
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
    env_identifier: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "envIdentifier",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "min_occurs": 1,
            "pattern": r"[a-zA-Z0-9_+\*\.]*:[a-zA-Z0-9_+\*\.]*:[a-zA-Z0-9_+\*\.]*",
        },
    )
    hierarchy_ref: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "name": "hierarchyRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    language: Optional["ViewType.Language"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    model_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelName",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    default_file_builder: Iterable[FileBuilderType] = field(
        default_factory=list,
        metadata={
            "name": "defaultFileBuilder",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    file_set_ref: Iterable[FileSetRef] = field(
        default_factory=list,
        metadata={
            "name": "fileSetRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    constraint_set_ref: Iterable[ConstraintSetRef] = field(
        default_factory=list,
        metadata={
            "name": "constraintSetRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    whitebox_element_refs: Optional["ViewType.WhiteboxElementRefs"] = field(
        default=None,
        metadata={
            "name": "whiteboxElementRefs",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    parameter: Iterable[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )

    @dataclass(slots=True)
    class Language:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        strict: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
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
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            },
        )
