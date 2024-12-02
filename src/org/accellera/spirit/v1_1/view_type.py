from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.constraint_set_ref import ConstraintSetRef
from org.accellera.spirit.v1_1.file_builder_type import FileBuilderType
from org.accellera.spirit.v1_1.file_set_ref import FileSetRef
from org.accellera.spirit.v1_1.parameter import Parameter
from org.accellera.spirit.v1_1.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class ViewType:
    """
    :ivar name: Name of the view. Must be unique within a component
    :ivar env_identifier: This is a string such as "ModelsimVerilog",
        used to uniquely identify the hardware environment. More than
        one indicates that the same information applies to multiple
        environments.
    :ivar language: The hardware description language used such as
        "verilog" or "vhdl". If the attribute "strict" is "true", this
        value must match the language being generated for the design.
    :ivar model_name: HDL-specific name to identify the model.
    :ivar default_file_builder:
    :ivar file_set_ref:
    :ivar constraint_set_ref:
    :ivar parameter:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "viewType"

    name: str = field(
        default="default",
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            "required": True,
        },
    )
    env_identifier: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "envIdentifier",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            "min_occurs": 1,
        },
    )
    language: Optional["ViewType.Language"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    model_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "modelName",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    default_file_builder: Iterable[FileBuilderType] = field(
        default_factory=list,
        metadata={
            "name": "defaultFileBuilder",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    file_set_ref: Iterable[FileSetRef] = field(
        default_factory=list,
        metadata={
            "name": "fileSetRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    constraint_set_ref: Iterable[ConstraintSetRef] = field(
        default_factory=list,
        metadata={
            "name": "constraintSetRef",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    parameter: Iterable[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
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
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            },
        )
