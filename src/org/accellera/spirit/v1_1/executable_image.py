from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.choice_style_value import ChoiceStyleValue
from org.accellera.spirit.v1_1.configurator_ref import ConfiguratorRef
from org.accellera.spirit.v1_1.direction_value import DirectionValue
from org.accellera.spirit.v1_1.file_builder_file_type import (
    FileBuilderFileType,
)
from org.accellera.spirit.v1_1.file_set_ref import FileSetRef
from org.accellera.spirit.v1_1.format_type import FormatType
from org.accellera.spirit.v1_1.generator_ref import GeneratorRef
from org.accellera.spirit.v1_1.parameter import Parameter
from org.accellera.spirit.v1_1.range_type_type import RangeTypeType
from org.accellera.spirit.v1_1.resolve_type import ResolveType
from org.accellera.spirit.v1_1.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class ExecutableImage:
    """Specifies an executable software image to be loaded into a processors
    address space.

    The format of the image is not specified. It could, for example, be
    an ELF loadfile, or it could be raw binary or ascii hex data for
    loading directly into a memory model instance.

    :ivar name: Name of the executable image file.
    :ivar parameter: Additional information about the load module, e.g.
        stack base addresses, table addresses, etc.
    :ivar language_tools: Default commands and flags for software
        language tools needed to build the executable image.
    :ivar file_set_ref_group: Contains a group of file set references
        that indicates the set of file sets complying with the tool set
        of the current executable image.
    :ivar vendor_extensions:
    :ivar id:
    :ivar image_type:
    """

    class Meta:
        name = "executableImage"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    name: Optional["ExecutableImage.Name"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    parameter: Iterable[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    language_tools: Optional["ExecutableImage.LanguageTools"] = field(
        default=None,
        metadata={
            "name": "languageTools",
            "type": "Element",
        },
    )
    file_set_ref_group: Optional["ExecutableImage.FileSetRefGroup"] = field(
        default=None,
        metadata={
            "name": "fileSetRefGroup",
            "type": "Element",
        },
    )
    vendor_extensions: Optional[VendorExtensions] = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
            "required": True,
        },
    )
    image_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "imageType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
        },
    )

    @dataclass(slots=True)
    class Name:
        """
        :ivar value:
        :ivar resolve:
        :ivar id:
        :ivar dependency:
        :ivar other_attributes:
        :ivar minimum: For user-resolved properties with numeric values,
            this indicates the minimum value allowed.
        :ivar maximum: For user-resolved properties with numeric values,
            this indicates the maximum value allowed.
        :ivar range_type:
        :ivar order: For components with auto-generated configuration
            forms, the user-resolved properties with order attibutes
            will be presented in ascending order.
        :ivar choice_ref: For user resolved properties with a "choice"
            format, this refers to a uiChoice element in the ui section
            of the component file.
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

    @dataclass(slots=True)
    class LanguageTools:
        """
        :ivar file_builder: A generic placeholder for any file builder
            like compilers and assemblers.  It contains the file types
            to which the command should be applied, and the flags to be
            used with that command.
        :ivar linker:
        :ivar linker_flags:
        :ivar linker_command_file: Specifies a linker command file.
        """

        file_builder: Iterable["ExecutableImage.LanguageTools.FileBuilder"] = (
            field(
                default_factory=list,
                metadata={
                    "name": "fileBuilder",
                    "type": "Element",
                },
            )
        )
        linker: Optional["ExecutableImage.LanguageTools.Linker"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        linker_flags: Optional["ExecutableImage.LanguageTools.LinkerFlags"] = (
            field(
                default=None,
                metadata={
                    "name": "linkerFlags",
                    "type": "Element",
                },
            )
        )
        linker_command_file: Optional[
            "ExecutableImage.LanguageTools.LinkerCommandFile"
        ] = field(
            default=None,
            metadata={
                "name": "linkerCommandFile",
                "type": "Element",
            },
        )

        @dataclass(slots=True)
        class FileBuilder:
            """
            :ivar file_type: Enumerated file types known by SPIRIT.
            :ivar user_file_type: Free form file type, not - yet - known
                by SPIRIT .
            :ivar command: Default command used to build files of the
                specified fileType.
            :ivar flags: Flags given to the build command when building
                files of this type.
            :ivar replace_default_flags: If true, replace any default
                flags value with the value in the sibling flags element.
                Otherwise, append the contents of the sibling flags
                element to any default flags value. If the value is true
                and the "flags" element is empty or missing, this will
                have the result of clearing any default flags value.
            :ivar vendor_extensions:
            """

            file_type: Optional[FileBuilderFileType] = field(
                default=None,
                metadata={
                    "name": "fileType",
                    "type": "Element",
                },
            )
            user_file_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "userFileType",
                    "type": "Element",
                },
            )
            command: Optional[
                "ExecutableImage.LanguageTools.FileBuilder.Command"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            flags: Optional[
                "ExecutableImage.LanguageTools.FileBuilder.Flags"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            replace_default_flags: Optional[
                "ExecutableImage.LanguageTools.FileBuilder.ReplaceDefaultFlags"
            ] = field(
                default=None,
                metadata={
                    "name": "replaceDefaultFlags",
                    "type": "Element",
                },
            )
            vendor_extensions: Optional[VendorExtensions] = field(
                default=None,
                metadata={
                    "name": "vendorExtensions",
                    "type": "Element",
                },
            )

            @dataclass(slots=True)
            class Command:
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

                value: str = field(
                    default="",
                    metadata={
                        "required": True,
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

            @dataclass(slots=True)
            class Flags:
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

                value: str = field(
                    default="",
                    metadata={
                        "required": True,
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

            @dataclass(slots=True)
            class ReplaceDefaultFlags:
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

                value: Optional[bool] = field(
                    default=None,
                    metadata={
                        "required": True,
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

        @dataclass(slots=True)
        class Linker:
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
                configuration forms, the user-resolved properties with
                order attibutes will be presented in ascending order.
            :ivar choice_ref: For user resolved properties with a
                "choice" format, this refers to a uiChoice element in
                the ui section of the component file.
            :ivar choice_style:
            :ivar direction:
            :ivar config_groups:
            :ivar format:
            :ivar prompt:
            """

            value: str = field(
                default="",
                metadata={
                    "required": True,
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

        @dataclass(slots=True)
        class LinkerFlags:
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
                configuration forms, the user-resolved properties with
                order attibutes will be presented in ascending order.
            :ivar choice_ref: For user resolved properties with a
                "choice" format, this refers to a uiChoice element in
                the ui section of the component file.
            :ivar choice_style:
            :ivar direction:
            :ivar config_groups:
            :ivar format:
            :ivar prompt:
            """

            value: str = field(
                default="",
                metadata={
                    "required": True,
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

        @dataclass(slots=True)
        class LinkerCommandFile:
            """
            :ivar name: Linker command file name.
            :ivar command_line_switch: The command line switch to
                specify the linker command file.
            :ivar enable: Specifies whether to generate and enable the
                linker command file.
            :ivar configurator_ref:
            :ivar generator_ref:
            """

            name: Optional[
                "ExecutableImage.LanguageTools.LinkerCommandFile.Name"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            command_line_switch: Optional[
                "ExecutableImage.LanguageTools.LinkerCommandFile.CommandLineSwitch"
            ] = field(
                default=None,
                metadata={
                    "name": "commandLineSwitch",
                    "type": "Element",
                    "required": True,
                },
            )
            enable: Optional[
                "ExecutableImage.LanguageTools.LinkerCommandFile.Enable"
            ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            configurator_ref: Optional[ConfiguratorRef] = field(
                default=None,
                metadata={
                    "name": "configuratorRef",
                    "type": "Element",
                },
            )
            generator_ref: Iterable[GeneratorRef] = field(
                default_factory=list,
                metadata={
                    "name": "generatorRef",
                    "type": "Element",
                },
            )

            @dataclass(slots=True)
            class Name:
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

            @dataclass(slots=True)
            class CommandLineSwitch:
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

                value: str = field(
                    default="",
                    metadata={
                        "required": True,
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

            @dataclass(slots=True)
            class Enable:
                """
                :ivar value:
                :ivar format: This is a hint to the user interface about
                    the data format to require for user resolved
                    properties. The bool.att attribute group sets the
                    default format to "bool".
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
    class FileSetRefGroup:
        file_set_ref: Iterable[FileSetRef] = field(
            default_factory=list,
            metadata={
                "name": "fileSetRef",
                "type": "Element",
            },
        )
