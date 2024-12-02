from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schemas.xmlsoap.org/soap/encoding/"


@dataclass(slots=True)
class Nmtokens:
    class Meta:
        name = "NMTOKENS"
        namespace = "http://schemas.xmlsoap.org/soap/encoding/"

    value: Iterable[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
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
