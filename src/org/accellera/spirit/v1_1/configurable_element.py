from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_1.choice_style_value import ChoiceStyleValue
from org.accellera.spirit.v1_1.direction_value import DirectionValue
from org.accellera.spirit.v1_1.format_type import FormatType
from org.accellera.spirit.v1_1.range_type_type import RangeTypeType
from org.accellera.spirit.v1_1.resolve_type import ResolveType

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"


@dataclass(slots=True)
class ConfigurableElement:
    """Describes the configurable content of an element in the instance.

    May contain text and/or child elements. The required referenceId
    attribute refers to the ID attribute of the configurable element.

    :ivar reference_id:
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
    :ivar content:
    """

    class Meta:
        name = "configurableElement"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1"

    reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "referenceId",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.1",
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
    content: Iterable[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "configurableElementValue",
                    "type": str,
                },
            ),
        },
    )
