from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.constraint_set_ref import ConstraintSetRef
from org.accellera.ipxact.v1685_2014.description import Description
from org.accellera.ipxact.v1685_2014.display_name import DisplayName
from org.accellera.ipxact.v1685_2014.file_builder_type import FileBuilderType
from org.accellera.ipxact.v1685_2014.file_set_ref import FileSetRef
from org.accellera.ipxact.v1685_2014.language_type import LanguageType
from org.accellera.ipxact.v1685_2014.module_parameter_type import (
    ModuleParameterType,
)
from org.accellera.ipxact.v1685_2014.parameters import Parameters
from org.accellera.ipxact.v1685_2014.vendor_extensions import VendorExtensions
from org.accellera.ipxact.v1685_2014.whitebox_element_ref_type import (
    WhiteboxElementRefType,
)

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class ComponentInstantiationType:
    """
    Component instantiation type.

    :ivar name: Unique name
    :ivar display_name:
    :ivar description:
    :ivar is_virtual: When true, indicates that this component should
        not be netlisted.
    :ivar language: The hardware description language used such as
        "verilog" or "vhdl". If the attribute "strict" is "true", this
        value must match the language being generated for the design.
    :ivar library_name: A string specifying the library name in which
        the model should be compiled. If the libraryName element is not
        present then its value defaults to “work”.
    :ivar package_name: A string describing the VHDL package containing
        the interface of the model. If the packageName element is not
        present then its value defaults to the component VLNV name
        concatenated with postfix “_cmp_pkg” which stands for component
        package.
    :ivar module_name: A string describing the Verilog, SystemVerilog,
        or SystemC module name or the VHDL entity name. If the
        moduleName is not present then its value defaults to the
        component VLNV name
    :ivar architecture_name: A string describing the VHDL architecture
        name. If the architectureName element is not present then its
        value defaults to “rtl”.
    :ivar configuration_name: A string describing the Verilog,
        SystemVerilog, or VHDL configuration name. If the
        configurationName element is not present then its value defaults
        to the design configuration VLNV name of the design
        configuration associated with the active hierarchical view or,
        if there is no active hierarchical view, to the component VLNV
        name concatenated with postfix “_rtl_cfg”.
    :ivar module_parameters: Model parameter name value pairs container
    :ivar default_file_builder: Default command and flags used to build
        derived files from the sourceName files in the referenced file
        sets.
    :ivar file_set_ref:
    :ivar constraint_set_ref:
    :ivar whitebox_element_refs: Container for white box element
        references.
    :ivar parameters:
    :ivar vendor_extensions:
    :ivar id:
    """

    class Meta:
        name = "componentInstantiationType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    is_virtual: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isVirtual",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    language: Optional[LanguageType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    library_name: Optional[object] = field(
        default=None,
        metadata={
            "name": "libraryName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    package_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "packageName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    module_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "moduleName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    architecture_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "architectureName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    configuration_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "configurationName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    module_parameters: Optional[
        "ComponentInstantiationType.ModuleParameters"
    ] = field(
        default=None,
        metadata={
            "name": "moduleParameters",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    default_file_builder: Iterable[FileBuilderType] = field(
        default_factory=list,
        metadata={
            "name": "defaultFileBuilder",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    file_set_ref: Iterable[FileSetRef] = field(
        default_factory=list,
        metadata={
            "name": "fileSetRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    constraint_set_ref: Iterable[ConstraintSetRef] = field(
        default_factory=list,
        metadata={
            "name": "constraintSetRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    whitebox_element_refs: Optional[
        "ComponentInstantiationType.WhiteboxElementRefs"
    ] = field(
        default=None,
        metadata={
            "name": "whiteboxElementRefs",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
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
    class ModuleParameters:
        """
        :ivar module_parameter: A module parameter name value pair. The
            name is given in an attribute. The value is the element
            value. The dataType (applicable to high level modeling) is
            given in the dataType attribute. For hardware based models,
            the name should be identical to the RTL (VHDL generic or
            Verilog parameter). The usageType attribute indicates how
            the model parameter is to be used.
        """

        module_parameter: Iterable[ModuleParameterType] = field(
            default_factory=list,
            metadata={
                "name": "moduleParameter",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
                "min_occurs": 1,
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
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            },
        )
