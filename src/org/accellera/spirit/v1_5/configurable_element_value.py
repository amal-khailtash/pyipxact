from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class ConfigurableElementValue:
    """Describes the content of a configurable element.

    The required referenceId attribute refers to the ID attribute of the
    configurable element.

    :ivar value:
    :ivar reference_id: Refers to the ID attribute of the configurable
        element.
    """

    class Meta:
        name = "configurableElementValue"
        namespace = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    reference_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "referenceId",
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5",
            "required": True,
        },
    )
