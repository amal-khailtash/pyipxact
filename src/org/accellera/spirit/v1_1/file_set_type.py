from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.choice_style_value import ChoiceStyleValue
from org.accellera.spirit.v1_1.data_type_type import DataTypeType
from org.accellera.spirit.v1_1.dependency import Dependency
from org.accellera.spirit.v1_1.direction_value import DirectionValue
from org.accellera.spirit.v1_1.file import File
from org.accellera.spirit.v1_1.file_builder_type import FileBuilderType
from org.accellera.spirit.v1_1.format_type import FormatType
from org.accellera.spirit.v1_1.library_ref_type import LibraryRefType
from org.accellera.spirit.v1_1.name_value_pair_type import NameValuePairType
from org.accellera.spirit.v1_1.range_type_type import RangeTypeType
from org.accellera.spirit.v1_1.resolve_type import ResolveType
from org.accellera.spirit.v1_1.source_file_file_type import SourceFileFileType
from org.accellera.spirit.v1_1.sw_function_return_type import (
    SwFunctionReturnType,
)
from org.accellera.spirit.v1_1.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class FileSetType:
    """
    :ivar owner: Specifies the original owner of the fileSet, used when
        importing fileSets from other components, as in Hierarchical
        components, to allow the parent component to correctly locate
        files imported from subcomponents
    :ivar group: Identifies this filleSet as belonging to a particular
        group or having a particular purpose. Examples might be
        "diagnostics", "boot", "application", "interrupt",
        "deviceDriver", etc.
    :ivar file:
    :ivar default_file_builder:
    :ivar dependency:
    :ivar sw_function: Generator information if this file set describes
        a sw function. For example, this file set may describe
        diagnostics for which the DE can generate a diagnostics driver.
        The boolean attribute "replicate", if true (default is false),
        directs the generator to compile a separate object module for
        each instance of the component in the design. Otherwise the
        single function will be called with different arguments for each
        instance (e.g. baseAddress).
    :ivar vendor_extensions:
    :ivar file_set_id:
    """

    class Meta:
        name = "fileSetType"

    owner: Optional[LibraryRefType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    group: Iterable[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    file: Iterable[File] = field(
        default_factory=list,
        metadata={
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
    dependency: Iterable[Dependency] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )
    sw_function: Optional["FileSetType.SwFunction"] = field(
        default=None,
        metadata={
            "name": "swFunction",
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
    file_set_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileSetId",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            "required": True,
        },
    )

    @dataclass(slots=True)
    class SwFunction:
        """
        :ivar entry_point:
        :ivar file_ref: A reference to the file that contains the entry
            point function.
        :ivar return_type: Function return type. See the enumerations.
        :ivar argument: Arguments passed in when the function is called.
            Arguments are passed in order. This is an extension of the
            name-value pair which includes the data type in the
            spirit:dataType attribute.  The argument name is in the
            spirit:name attribute and its value is in the text content
            of the element.
        :ivar enabled: Specifies if the SW function is enabled. Default
            is true.
        :ivar source_file:
        :ivar replicate:
        """

        entry_point: Optional[str] = field(
            default=None,
            metadata={
                "name": "entryPoint",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            },
        )
        file_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "fileRef",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                "required": True,
            },
        )
        return_type: Optional[SwFunctionReturnType] = field(
            default=None,
            metadata={
                "name": "returnType",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            },
        )
        argument: Iterable["FileSetType.SwFunction.Argument"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            },
        )
        enabled: Optional["FileSetType.SwFunction.Enabled"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            },
        )
        source_file: Iterable["FileSetType.SwFunction.SourceFile"] = field(
            default_factory=list,
            metadata={
                "name": "sourceFile",
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            },
        )
        replicate: Optional[bool] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            },
        )

        @dataclass(slots=True)
        class Argument(NameValuePairType):
            data_type: Optional[DataTypeType] = field(
                default=None,
                metadata={
                    "name": "dataType",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    "required": True,
                },
            )

        @dataclass(slots=True)
        class Enabled:
            """
            :ivar value:
            :ivar format: This is a hint to the user interface about the
                data format to require for user resolved properties. The
                bool.att attribute group sets the default format to
                "bool".
            :ivar resolve:
            :ivar id:
            :ivar dependency:
            :ivar other_attributes:
            :ivar minimum: For user-resolved properties with numeric
                values, this indicates the minimum value allowed.
            :ivar maximum: For user-resolved properties with numeric
                values, this indicates the maximum value allowed.
            :ivar range_type:
            :ivar order: For components with auto-generated
                configuration forms, the user-resolved properties with
                order attibutes will be presented in ascending order.
            :ivar choice_ref: For user resolved properties with a
                "choice" format, this refers to a uiChoice element in
                the ui section of the component file.
            :ivar choice_style:
            :ivar direction:
            :ivar config_groups:
            :ivar prompt:
            """

            value: Optional[bool] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )
            format: FormatType = field(
                default=FormatType.BOOL,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            resolve: Optional[ResolveType] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            dependency: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            other_attributes: Mapping[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##other",
                },
            )
            minimum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            maximum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            range_type: Optional[RangeTypeType] = field(
                default=None,
                metadata={
                    "name": "rangeType",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            order: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            choice_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "choiceRef",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            choice_style: Optional[ChoiceStyleValue] = field(
                default=None,
                metadata={
                    "name": "choiceStyle",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            direction: Optional[DirectionValue] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            config_groups: Iterable[str] = field(
                default_factory=list,
                metadata={
                    "name": "configGroups",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    "tokens": True,
                },
            )
            prompt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )

        @dataclass(slots=True)
        class SourceFile:
            """
            :ivar source_name: Source file for the boot load.  Relative
                names are searched for in the project directory and the
                source of the component directory.
            :ivar file_type: Enumerated file types known by SPIRIT.
            :ivar user_file_type: Free form file type, not - yet - known
                by SPIRIT .
            """

            source_name: Optional[
                "FileSetType.SwFunction.SourceFile.SourceName"
            ] = field(
                default=None,
                metadata={
                    "name": "sourceName",
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    "required": True,
                },
            )
            file_type: Optional[SourceFileFileType] = field(
                default=None,
                metadata={
                    "name": "fileType",
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )
            user_file_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "userFileType",
                    "type": "Element",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                },
            )

            @dataclass(slots=True)
            class SourceName:
                """
                :ivar value:
                :ivar resolve:
                :ivar id:
                :ivar dependency:
                :ivar other_attributes:
                :ivar minimum: For user-resolved properties with numeric
                    values, this indicates the minimum value allowed.
                :ivar maximum: For user-resolved properties with numeric
                    values, this indicates the maximum value allowed.
                :ivar range_type:
                :ivar order: For components with auto-generated
                    configuration forms, the user-resolved properties
                    with order attibutes will be presented in ascending
                    order.
                :ivar choice_ref: For user resolved properties with a
                    "choice" format, this refers to a uiChoice element
                    in the ui section of the component file.
                :ivar choice_style:
                :ivar direction:
                :ivar config_groups:
                :ivar format:
                :ivar prompt:
                """

                value: str = field(default="")
                resolve: Optional[ResolveType] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                dependency: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                other_attributes: Mapping[str, str] = field(
                    default_factory=dict,
                    metadata={
                        "type": "Attributes",
                        "namespace": "##other",
                    },
                )
                minimum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                maximum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                range_type: Optional[RangeTypeType] = field(
                    default=None,
                    metadata={
                        "name": "rangeType",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                order: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                choice_ref: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "choiceRef",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                choice_style: Optional[ChoiceStyleValue] = field(
                    default=None,
                    metadata={
                        "name": "choiceStyle",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                direction: Optional[DirectionValue] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                config_groups: Iterable[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "configGroups",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                        "tokens": True,
                    },
                )
                format: Optional[FormatType] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
                prompt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
                    },
                )
