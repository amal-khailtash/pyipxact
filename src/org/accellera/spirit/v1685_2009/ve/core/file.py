from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.core.dependency import Dependency
from org.accellera.spirit.v1685_2009.ve.core.file_file_type import FileFileType
from org.accellera.spirit.v1685_2009.ve.core.format_type import FormatType
from org.accellera.spirit.v1685_2009.ve.core.name_value_pair_type_1 import (
    NameValuePairType1,
)
from org.accellera.spirit.v1685_2009.ve.core.range_type_type import (
    RangeTypeType,
)
from org.accellera.spirit.v1685_2009.ve.core.resolve_type import ResolveType
from org.accellera.spirit.v1685_2009.ve.core.vendor_extensions import (
    VendorExtensions,
)

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class File:
    """
    IP-XACT reference to a file or directory.

    :ivar name: Path to the file or directory. If this path is a
        relative path, then it is relative to the containing XML file.
    :ivar file_type: Enumerated file types known by IP-XACT.
    :ivar user_file_type: Free form file type, not - yet - known by IP-
        XACT .
    :ivar is_include_file: Indicate that the file is include file.
    :ivar logical_name: Logical name for this file or directory e.g.
        VHDL library name.
    :ivar exported_name: Defines exported names that can be accessed
        externally, e.g. exported function names from a C source file.
    :ivar build_command: Command and flags used to build derived files
        from the sourceName files. If this element is present, the
        command and/or flags used to to build the file will override or
        augment any default builders at a higher level.
    :ivar dependency:
    :ivar define: Specifies define symbols that are used in the source
        file.  The spirit:name element gives the name to be defined and
        the text content of the spirit:value element holds the value.
        This element supports full configurability.
    :ivar image_type: Relates the current file to a certain executable
        image type in the design.
    :ivar description: String for describing this file to users
    :ivar vendor_extensions:
    :ivar file_id: Unique ID for this file, referenced in
        fileSet/function/fileRef
    :ivar any_attributes:
    """

    class Meta:
        name = "file"
        namespace = (
            "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"
        )

    name: Optional["File.Name"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    file_type: Iterable[FileFileType] = field(
        default_factory=list,
        metadata={
            "name": "fileType",
            "type": "Element",
        },
    )
    user_file_type: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "userFileType",
            "type": "Element",
        },
    )
    is_include_file: Optional["File.IsIncludeFile"] = field(
        default=None,
        metadata={
            "name": "isIncludeFile",
            "type": "Element",
        },
    )
    logical_name: Optional["File.LogicalName"] = field(
        default=None,
        metadata={
            "name": "logicalName",
            "type": "Element",
        },
    )
    exported_name: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "exportedName",
            "type": "Element",
        },
    )
    build_command: Optional["File.BuildCommand"] = field(
        default=None,
        metadata={
            "name": "buildCommand",
            "type": "Element",
        },
    )
    dependency: Iterable[Dependency] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    define: Iterable[NameValuePairType1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    image_type: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "imageType",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
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
    file_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileId",
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
    class IsIncludeFile:
        """
        :ivar value:
        :ivar external_declarations: the File contains some declarations
            that are needed in top file
        """

        value: Optional[bool] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
        external_declarations: bool = field(
            default=False,
            metadata={
                "name": "externalDeclarations",
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            },
        )

    @dataclass(slots=True)
    class LogicalName:
        """
        :ivar value:
        :ivar default: The logical name shall only be used as a default
            and another process may override this name.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        default: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            },
        )

    @dataclass(slots=True)
    class BuildCommand:
        """
        :ivar command: Command used to build this file.
        :ivar flags: Flags given to the build command when building this
            file. If the optional attribute "append" is "true", this
            string will be appended to any existing flags, otherwise
            these flags will replace any existing default flags.
        :ivar replace_default_flags: If true, the value of the sibling
            element "flags" should replace any default flags specified
            at a more global level. If this is true and the sibling
            element "flags" is empty or missing, this has the effect of
            clearing any default flags.
        :ivar target_name: Pathname to the file that is derived (built)
            from the source file.
        """

        command: Optional["File.BuildCommand.Command"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        flags: Optional["File.BuildCommand.Flags"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        replace_default_flags: Optional[
            "File.BuildCommand.ReplaceDefaultFlags"
        ] = field(
            default=None,
            metadata={
                "name": "replaceDefaultFlags",
                "type": "Element",
            },
        )
        target_name: Optional["File.BuildCommand.TargetName"] = field(
            default=None,
            metadata={
                "name": "targetName",
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
            """
            :ivar value:
            :ivar append: "true" indicates that the flags shall be
                appended to any existing flags, "false"indicates these
                flags will replace any existing default flags.
            :ivar format:
            :ivar resolve:
            :ivar id:
            :ivar dependency:
            :ivar any_attributes:
            :ivar choice_ref:
            :ivar order:
            :ivar config_groups:
            :ivar bit_string_length:
            :ivar minimum:
            :ivar maximum:
            :ivar range_type:
            :ivar prompt:
            """

            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            append: Optional[bool] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
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
        class TargetName:
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
