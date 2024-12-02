from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_0.choice_style_value import ChoiceStyleValue
from org.accellera.spirit.v1_0.direction_value import DirectionValue
from org.accellera.spirit.v1_0.format_type import FormatType
from org.accellera.spirit.v1_0.range_type_type import RangeTypeType
from org.accellera.spirit.v1_0.resolve_type import ResolveType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class NameValuePairType:
    """Used wherever a name value pair is appropriate.

    The name is given by the attribute while the value is the element
    content. Supports configurability attributes and a cross reference
    XPath expression.

    :ivar value:
    :ivar name: The name in a name-value pair.
    :ivar cross_ref:
    :ivar resolve:
    :ivar id:
    :ivar dependency:
    :ivar other_attributes:
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
    :ivar format:
    :ivar prompt:
    """

    class Meta:
        name = "nameValuePairType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
    cross_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "crossRef",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    resolve: Optional[ResolveType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    dependency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
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
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    maximum: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    range_type: Optional[RangeTypeType] = field(
        default=None,
        metadata={
            "name": "rangeType",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    order: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    choice_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "choiceRef",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    choice_style: Optional[ChoiceStyleValue] = field(
        default=None,
        metadata={
            "name": "choiceStyle",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    direction: Optional[DirectionValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    config_groups: Iterable[str] = field(
        default_factory=list,
        metadata={
            "name": "configGroups",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "tokens": True,
        },
    )
    format: Optional[FormatType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
    prompt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
        },
    )
