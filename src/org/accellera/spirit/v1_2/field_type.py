from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.access import Access
from org.accellera.spirit.v1_2.choice_style_value import ChoiceStyleValue
from org.accellera.spirit.v1_2.direction_value import DirectionValue
from org.accellera.spirit.v1_2.format_type import FormatType
from org.accellera.spirit.v1_2.parameter import Parameter
from org.accellera.spirit.v1_2.range_type_type import RangeTypeType
from org.accellera.spirit.v1_2.resolve_type import ResolveType
from org.accellera.spirit.v1_2.vendor_extensions import VendorExtensions

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class FieldType:
    """
    :ivar name: Field name.
    :ivar bit_offset: Offset of this field's lsb from bit 0 of the
        register.
    :ivar bit_width: Width of the field in bits.
    :ivar access:
    :ivar description: Bit field description.
    :ivar values: Enumerates specific values that can be assigned to the
        bit field.
    :ivar parameter:
    :ivar vendor_extensions:
    """

    class Meta:
        name = "fieldType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
    bit_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "bitOffset",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
    bit_width: Optional["FieldType.BitWidth"] = field(
        default=None,
        metadata={
            "name": "bitWidth",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
            "required": True,
        },
    )
    access: Optional[Access] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
        },
    )
    values: Iterable["FieldType.Values"] = field(
        default_factory=list,
        metadata={
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
    class BitWidth:
        """
        :ivar value:
        :ivar format: This is a hint to the user interface about the
            data format to require for user resolved properties. The
            long.att attribute group sets the default format to "long".
        :ivar resolve:
        :ivar id:
        :ivar dependency:
        :ivar any_attributes:
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

    @dataclass(slots=True)
    class Values:
        """
        :ivar value: Enumerated bit field value.
        :ivar description: Description of a bit field value.
        :ivar name: The name of this enumerated value. This may be used
            as a token in generating code.
        """

        value: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                "required": True,
                "pattern": r"-?((0x)|(0X)|#)?[0-9a-fA-F]*[kmgtKMGT]?",
            },
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                "required": True,
            },
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2",
                "required": True,
            },
        )