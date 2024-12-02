from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.power.file_builder_file_type import (
    FileBuilderFileType,
)
from org.accellera.spirit.v1685_2009.ve.power.file_set_ref import FileSetRef
from org.accellera.spirit.v1685_2009.ve.power.format_type import FormatType
from org.accellera.spirit.v1685_2009.ve.power.generator_ref import GeneratorRef
from org.accellera.spirit.v1685_2009.ve.power.parameters import Parameters
from org.accellera.spirit.v1685_2009.ve.power.range_type_type import (
    RangeTypeType,
)
from org.accellera.spirit.v1685_2009.ve.power.resolve_type import ResolveType
from org.accellera.spirit.v1685_2009.ve.power.vendor_extensions import (
    VendorExtensions,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class ExecutableImage:
    """Specifies an executable software image to be loaded into a processors
    address space.

    The format of the image is not specified. It could, for example, be
    an ELF loadfile, or it could be raw binary or ascii hex data for
    loading directly into a memory model instance.

    :ivar name: Name of the executable image file.
    :ivar description: String for describing this executable image to
        users
    :ivar parameters: Additional information about the load module, e.g.
        stack base addresses, table addresses, etc.
    :ivar language_tools: Default commands and flags for software
        language tools needed to build the executable image.
    :ivar file_set_ref_group: Contains a group of file set references
        that indicates the set of file sets complying with the tool set
        of the current executable image.
    :ivar vendor_extensions:
    :ivar id: Unique ID for the executableImage, referenced in
        fileSet/function/fileRef
    :ivar image_type: Open element to describe the type of image. The
        contents is model and/or generator specific.
    """

    class Meta:
        name = "executableImage"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
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
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "required": True,
        },
    )
    image_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "imageType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
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
            :ivar file_type: Enumerated file types known by IP-XACT.
            :ivar user_file_type: Free form file type, not - yet - known
                by IP-XACT .
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
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    },
                )
                format: FormatType = field(
                    default=FormatType.STRING,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                resolve: ResolveType = field(
                    default=ResolveType.IMMEDIATE,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                dependency: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                any_attributes: Mapping[str, str] = field(
                    default_factory=dict,
                    metadata={
                        "type": "Attributes",
                        "namespace": "##any",
                    },
                )
                choice_ref: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "choiceRef",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                order: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                config_groups: Iterable[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "configGroups",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                        "tokens": True,
                    },
                )
                bit_string_length: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "bitStringLength",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                minimum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                maximum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                range_type: RangeTypeType = field(
                    default=RangeTypeType.FLOAT,
                    metadata={
                        "name": "rangeType",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                prompt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )

            @dataclass(slots=True)
            class Flags:
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    },
                )
                format: FormatType = field(
                    default=FormatType.STRING,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                resolve: ResolveType = field(
                    default=ResolveType.IMMEDIATE,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                dependency: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                any_attributes: Mapping[str, str] = field(
                    default_factory=dict,
                    metadata={
                        "type": "Attributes",
                        "namespace": "##any",
                    },
                )
                choice_ref: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "choiceRef",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                order: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                config_groups: Iterable[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "configGroups",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                        "tokens": True,
                    },
                )
                bit_string_length: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "bitStringLength",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                minimum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                maximum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                range_type: RangeTypeType = field(
                    default=RangeTypeType.FLOAT,
                    metadata={
                        "name": "rangeType",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                prompt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )

            @dataclass(slots=True)
            class ReplaceDefaultFlags:
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
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                resolve: ResolveType = field(
                    default=ResolveType.IMMEDIATE,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                dependency: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                any_attributes: Mapping[str, str] = field(
                    default_factory=dict,
                    metadata={
                        "type": "Attributes",
                        "namespace": "##any",
                    },
                )
                choice_ref: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "choiceRef",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                order: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                config_groups: Iterable[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "configGroups",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                        "tokens": True,
                    },
                )
                bit_string_length: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "bitStringLength",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                minimum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                maximum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                range_type: RangeTypeType = field(
                    default=RangeTypeType.INT,
                    metadata={
                        "name": "rangeType",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                prompt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )

        @dataclass(slots=True)
        class Linker:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            format: FormatType = field(
                default=FormatType.STRING,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            resolve: ResolveType = field(
                default=ResolveType.IMMEDIATE,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            dependency: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            any_attributes: Mapping[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )
            choice_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "choiceRef",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            order: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            config_groups: Iterable[str] = field(
                default_factory=list,
                metadata={
                    "name": "configGroups",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    "tokens": True,
                },
            )
            bit_string_length: Optional[int] = field(
                default=None,
                metadata={
                    "name": "bitStringLength",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            minimum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            maximum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            range_type: RangeTypeType = field(
                default=RangeTypeType.FLOAT,
                metadata={
                    "name": "rangeType",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            prompt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )

        @dataclass(slots=True)
        class LinkerFlags:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            format: FormatType = field(
                default=FormatType.STRING,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            resolve: ResolveType = field(
                default=ResolveType.IMMEDIATE,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            dependency: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            any_attributes: Mapping[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )
            choice_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "choiceRef",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            order: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            config_groups: Iterable[str] = field(
                default_factory=list,
                metadata={
                    "name": "configGroups",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    "tokens": True,
                },
            )
            bit_string_length: Optional[int] = field(
                default=None,
                metadata={
                    "name": "bitStringLength",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            minimum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            maximum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            range_type: RangeTypeType = field(
                default=RangeTypeType.FLOAT,
                metadata={
                    "name": "rangeType",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                },
            )
            prompt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
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
            :ivar generator_ref:
            :ivar vendor_extensions:
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
            generator_ref: Iterable[GeneratorRef] = field(
                default_factory=list,
                metadata={
                    "name": "generatorRef",
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
            class Name:
                value: str = field(default="")
                format: FormatType = field(
                    default=FormatType.STRING,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                resolve: ResolveType = field(
                    default=ResolveType.IMMEDIATE,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                dependency: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                any_attributes: Mapping[str, str] = field(
                    default_factory=dict,
                    metadata={
                        "type": "Attributes",
                        "namespace": "##any",
                    },
                )
                choice_ref: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "choiceRef",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                order: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                config_groups: Iterable[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "configGroups",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                        "tokens": True,
                    },
                )
                bit_string_length: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "bitStringLength",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                minimum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                maximum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                range_type: RangeTypeType = field(
                    default=RangeTypeType.FLOAT,
                    metadata={
                        "name": "rangeType",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                prompt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )

            @dataclass(slots=True)
            class CommandLineSwitch:
                value: str = field(
                    default="",
                    metadata={
                        "required": True,
                    },
                )
                format: FormatType = field(
                    default=FormatType.STRING,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                resolve: ResolveType = field(
                    default=ResolveType.IMMEDIATE,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                dependency: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                any_attributes: Mapping[str, str] = field(
                    default_factory=dict,
                    metadata={
                        "type": "Attributes",
                        "namespace": "##any",
                    },
                )
                choice_ref: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "choiceRef",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                order: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                config_groups: Iterable[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "configGroups",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                        "tokens": True,
                    },
                )
                bit_string_length: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "bitStringLength",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                minimum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                maximum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                range_type: RangeTypeType = field(
                    default=RangeTypeType.FLOAT,
                    metadata={
                        "name": "rangeType",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                prompt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )

            @dataclass(slots=True)
            class Enable:
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
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                resolve: ResolveType = field(
                    default=ResolveType.IMMEDIATE,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                id: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                dependency: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                any_attributes: Mapping[str, str] = field(
                    default_factory=dict,
                    metadata={
                        "type": "Attributes",
                        "namespace": "##any",
                    },
                )
                choice_ref: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "choiceRef",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                order: Optional[float] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                config_groups: Iterable[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "configGroups",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                        "tokens": True,
                    },
                )
                bit_string_length: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "bitStringLength",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                minimum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                maximum: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                range_type: RangeTypeType = field(
                    default=RangeTypeType.INT,
                    metadata={
                        "name": "rangeType",
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )
                prompt: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
                    },
                )

    @dataclass(slots=True)
    class FileSetRefGroup:
        file_set_ref: Iterable[FileSetRef] = field(
            default_factory=list,
            metadata={
                "name": "fileSetRef",
                "type": "Element",
                "min_occurs": 1,
            },
        )
