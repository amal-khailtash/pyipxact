from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schemas.xmlsoap.org/soap/encoding/"


@dataclass(slots=True)
class PositiveInteger:
    class Meta:
        name = "positiveInteger"
        namespace = "http://schemas.xmlsoap.org/soap/encoding/"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Mapping[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
