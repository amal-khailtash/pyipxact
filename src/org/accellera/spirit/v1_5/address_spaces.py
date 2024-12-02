from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_5.address_unit_bits import AddressUnitBits
from org.accellera.spirit.v1_5.description import Description
from org.accellera.spirit.v1_5.display_name import DisplayName
from org.accellera.spirit.v1_5.executable_image import ExecutableImage
from org.accellera.spirit.v1_5.format_type import FormatType
from org.accellera.spirit.v1_5.local_memory_map_type import LocalMemoryMapType
from org.accellera.spirit.v1_5.parameters import Parameters
from org.accellera.spirit.v1_5.range_type_type import RangeTypeType
from org.accellera.spirit.v1_5.resolve_type import ResolveType
from org.accellera.spirit.v1_5.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


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
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

    address_space: Iterable["AddressSpaces.AddressSpace"] = field(
        default_factory=list,
        metadata={
            "name": "addressSpace",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass(slots=True)
    class AddressSpace:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar description:
        :ivar range: The address range of an address block.  Expressed
            as the number of addressable units accessible to the block.
            The range and the width are related by the following
            formulas: number_of_bits_in_block = spirit:addressUnitBits *
            spirit:range number_of_rows_in_block =
            number_of_bits_in_block / spirit:width
        :ivar width: The bit width of a row in the address block. The
            range and the width are related by the following formulas:
            number_of_bits_in_block = spirit:addressUnitBits *
            spirit:range number_of_rows_in_block =
            number_of_bits_in_block / spirit:width
        :ivar segments: Address segments withing an addressSpace
        :ivar address_unit_bits:
        :ivar executable_image:
        :ivar local_memory_map: Provides the local memory map of an
            address space.  Blocks in this memory map are accessable to
            master interfaces on this component that reference this
            address space.   They are not accessable to any external
            master interface.
        :ivar parameters: Data specific to this address space.
        :ivar vendor_extensions:
        """

        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        display_name: Optional[DisplayName] = field(
            default=None,
            metadata={
                "name": "displayName",
                "type": "Element",
            },
        )
        description: Optional[Description] = field(
            default=None,
            metadata={
                "type": "Element",
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
        segments: Optional["AddressSpaces.AddressSpace.Segments"] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        address_unit_bits: Optional[AddressUnitBits] = field(
            default=None,
            metadata={
                "name": "addressUnitBits",
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
        parameters: Optional[Parameters] = field(
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

        @dataclass(slots=True)
        class Segments:
            """
            :ivar segment: Address segment withing an addressSpace
            """

            segment: Iterable[
                "AddressSpaces.AddressSpace.Segments.Segment"
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass(slots=True)
            class Segment:
                """
                :ivar name: Unique name
                :ivar display_name:
                :ivar description:
                :ivar address_offset: Address offset of the segment
                    within the containing address space.
                :ivar range: The address range of asegment.  Expressed
                    as the number of addressable units accessible to the
                    segment.
                :ivar vendor_extensions:
                """

                name: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    },
                )
                display_name: Optional[DisplayName] = field(
                    default=None,
                    metadata={
                        "name": "displayName",
                        "type": "Element",
                    },
                )
                description: Optional[Description] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                address_offset: Optional[
                    "AddressSpaces.AddressSpace.Segments.Segment.AddressOffset"
                ] = field(
                    default=None,
                    metadata={
                        "name": "addressOffset",
                        "type": "Element",
                        "required": True,
                    },
                )
                range: Optional[
                    "AddressSpaces.AddressSpace.Segments.Segment.Range"
                ] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
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
                class AddressOffset:
                    value: str = field(
                        default="",
                        metadata={
                            "required": True,
                            "pattern": r"[+]?(0x|0X|#)?[0-9a-fA-F]+[kmgtKMGT]?",
                        },
                    )
                    format: FormatType = field(
                        default=FormatType.LONG,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    resolve: ResolveType = field(
                        default=ResolveType.IMMEDIATE,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    id: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    dependency: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
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
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    order: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    config_groups: Iterable[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "configGroups",
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                            "tokens": True,
                        },
                    )
                    bit_string_length: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "bitStringLength",
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    minimum: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    maximum: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    range_type: RangeTypeType = field(
                        default=RangeTypeType.FLOAT,
                        metadata={
                            "name": "rangeType",
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    prompt: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )

                @dataclass(slots=True)
                class Range:
                    value: str = field(
                        default="",
                        metadata={
                            "required": True,
                            "pattern": r"[+]?(0x|0X|#)?[0]*[1-9a-fA-F][0-9a-fA-F]*[kmgtKMGT]?",
                        },
                    )
                    format: FormatType = field(
                        default=FormatType.LONG,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    resolve: ResolveType = field(
                        default=ResolveType.IMMEDIATE,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    id: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    dependency: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
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
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    order: Optional[float] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    config_groups: Iterable[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "configGroups",
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                            "tokens": True,
                        },
                    )
                    bit_string_length: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "bitStringLength",
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    minimum: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    maximum: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    range_type: RangeTypeType = field(
                        default=RangeTypeType.FLOAT,
                        metadata={
                            "name": "rangeType",
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )
                    prompt: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Attribute",
                            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                        },
                    )

        @dataclass(slots=True)
        class Range:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                    "pattern": r"[+]?(0x|0X|#)?[0]*[1-9a-fA-F][0-9a-fA-F]*[kmgtKMGT]?",
                },
            )
            format: FormatType = field(
                default=FormatType.LONG,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            resolve: ResolveType = field(
                default=ResolveType.IMMEDIATE,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            dependency: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
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
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            order: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            config_groups: Iterable[str] = field(
                default_factory=list,
                metadata={
                    "name": "configGroups",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                    "tokens": True,
                },
            )
            bit_string_length: Optional[int] = field(
                default=None,
                metadata={
                    "name": "bitStringLength",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            minimum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            maximum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            range_type: RangeTypeType = field(
                default=RangeTypeType.FLOAT,
                metadata={
                    "name": "rangeType",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            prompt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )

        @dataclass(slots=True)
        class Width:
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
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            resolve: ResolveType = field(
                default=ResolveType.IMMEDIATE,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            id: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            dependency: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
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
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            order: Optional[float] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            config_groups: Iterable[str] = field(
                default_factory=list,
                metadata={
                    "name": "configGroups",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                    "tokens": True,
                },
            )
            bit_string_length: Optional[int] = field(
                default=None,
                metadata={
                    "name": "bitStringLength",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            minimum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            maximum: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            range_type: RangeTypeType = field(
                default=RangeTypeType.FLOAT,
                metadata={
                    "name": "rangeType",
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
            prompt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
                },
            )
