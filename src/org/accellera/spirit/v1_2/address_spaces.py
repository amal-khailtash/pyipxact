from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.bits_in_lau import BitsInLau
from org.accellera.spirit.v1_2.choice_style_value import ChoiceStyleValue
from org.accellera.spirit.v1_2.direction_value import DirectionValue
from org.accellera.spirit.v1_2.endianess_type import EndianessType
from org.accellera.spirit.v1_2.executable_image import ExecutableImage
from org.accellera.spirit.v1_2.format_type import FormatType
from org.accellera.spirit.v1_2.local_memory_map_type import LocalMemoryMapType
from org.accellera.spirit.v1_2.name_value_pair_type import NameValuePairType
from org.accellera.spirit.v1_2.range_type_type import RangeTypeType
from org.accellera.spirit.v1_2.resolve_type import ResolveType
from org.accellera.spirit.v1_2.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class AddressSpaces:
    """
    If this component is a bus master, this lists all the address spaces defined by
    the component.

    :ivar address_space: This defines a logical space, referenced by a
        bus master.
    """

    class Meta:
        name = "addressSpaces"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

    address_space: Iterable["AddressSpaces.AddressSpace"] = field(
        default_factory=list,
        metadata={
            "name": "addressSpace",
            "type": "Element",
        },
    )

    @dataclass(slots=True)
    class AddressSpace:
        """
        :ivar name: The name of the address space.  Unique within the
            model.
        :ivar range: The address range of an address block.  Expressed
            as the number of addressable units accessable to the block.
        :ivar width: Bit width of an address block.
        :ivar bits_in_lau:
        :ivar endianness:
        :ivar executable_image:
        :ivar local_memory_map: Provides the local memory map of an
            address space.  Blocks in this memory map are accessable to
            master interfaces on this component that reference this
            address space.   They are not accessable to any external
            master interface.
        :ivar parameter: Data specific to this address space.
        :ivar vendor_extensions:
        """

        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        range: Optional["AddressSpaces.AddressSpace.Range"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        width: Optional["AddressSpaces.AddressSpace.Width"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        bits_in_lau: Optional[BitsInLau] = field(
            default=None,
            metadata={
                "name": "bitsInLau",
                "type": "Element",
            },
        )
        endianness: Optional[EndianessType] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        executable_image: Iterable[ExecutableImage] = field(
            default_factory=list,
            metadata={
                "name": "executableImage",
                "type": "Element",
            },
        )
        local_memory_map: Optional[LocalMemoryMapType] = field(
            default=None,
            metadata={
                "name": "localMemoryMap",
                "type": "Element",
            },
        )
        parameter: Iterable[NameValuePairType] = field(
            default_factory=list,
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

        @dataclass(slots=True)
        class Range:
            """
            :ivar value:
            :ivar format: This is a hint to the user interface about the
                data format to require for user resolved properties. The
                long.att attribute group sets the default format to
                "long".
            :ivar resolve:
            :ivar id:
            :ivar dependency:
            :ivar any_attributes:
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

            value: str = field(
                default="",
                metadata={
                    "required": True,
                    "pattern": r"-?((0x)|(0X)|#)?[0-9a-fA-F]*[kmgtKMGT]?",
                },
            )
            format: FormatType = field(
                default=FormatType.LONG,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            resolve: ResolveType = field(
                default=ResolveType.IMMEDIATE,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            dependency: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            any_attributes: Mapping[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )
            minimum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            maximum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            range_type: RangeTypeType = field(
                default=RangeTypeType.FLOAT,
                metadata={
                    "name": "rangeType",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            order: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            choice_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "choiceRef",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            choice_style: Optional[ChoiceStyleValue] = field(
                default=None,
                metadata={
                    "name": "choiceStyle",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            direction: Optional[DirectionValue] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            config_groups: Iterable[str] = field(
                default_factory=list,
                metadata={
                    "name": "configGroups",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                    "tokens": True,
                },
            )
            prompt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )

        @dataclass(slots=True)
        class Width:
            """
            :ivar value:
            :ivar format: This is a hint to the user interface about the
                data format to require for user resolved properties. The
                long.att attribute group sets the default format to
                "long".
            :ivar resolve:
            :ivar id:
            :ivar dependency:
            :ivar any_attributes:
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

            value: Optional[int] = field(
                default=None,
                metadata={
                    "required": True,
                },
            )
            format: FormatType = field(
                default=FormatType.LONG,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            resolve: ResolveType = field(
                default=ResolveType.IMMEDIATE,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            dependency: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            any_attributes: Mapping[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )
            minimum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            maximum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            range_type: RangeTypeType = field(
                default=RangeTypeType.FLOAT,
                metadata={
                    "name": "rangeType",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            order: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            choice_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "choiceRef",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            choice_style: Optional[ChoiceStyleValue] = field(
                default=None,
                metadata={
                    "name": "choiceStyle",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            direction: Optional[DirectionValue] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )
            config_groups: Iterable[str] = field(
                default_factory=list,
                metadata={
                    "name": "configGroups",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                    "tokens": True,
                },
            )
            prompt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                },
            )