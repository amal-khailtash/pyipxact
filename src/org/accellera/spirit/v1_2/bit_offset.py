from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_2.choice_style_value import ChoiceStyleValue
from org.accellera.spirit.v1_2.direction_value import DirectionValue
from org.accellera.spirit.v1_2.format_type import FormatType
from org.accellera.spirit.v1_2.range_type_type import RangeTypeType
from org.accellera.spirit.v1_2.resolve_type import ResolveType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"


@dataclass(slots=True)
class BitOffset:
    """Base bit offset of an address block.

    If not included, it is assumed to be 0.

    :ivar value:
    :ivar format: This is a hint to the user interface about the data
        format to require for user resolved properties. The long.att
        attribute group sets the default format to "long".
    :ivar resolve:
    :ivar id:
    :ivar dependency:
    :ivar any_attributes:
    :ivar minimum: For user-resolved properties with numeric values,
        this indicates the minimum value allowed.
    :ivar maximum: For user-resolved properties with numeric values,
        this indicates the maximum value allowed.
    :ivar range_type:
    :ivar order: For components with auto-generated configuration forms,
        the user-resolved properties with order attibutes will be
        presented in ascending order.
    :ivar choice_ref: For user resolved properties with a "choice"
        format, this refers to a uiChoice element in the ui section of
        the component file.
    :ivar choice_style:
    :ivar direction:
    :ivar config_groups:
    :ivar prompt:
    """

    class Meta:
        name = "bitOffset"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.2"

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
