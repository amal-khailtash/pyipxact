from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schemas.xmlsoap.org/soap/encoding/"


@dataclass(slots=True)
class Array:
    """
    'Array' is a complex type for accessors identified by position.
    """

    class Meta:
        namespace = "http://schemas.xmlsoap.org/soap/encoding/"

    any_element: Iterable[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    array_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "arrayType",
            "type": "Attribute",
            "namespace": "http://schemas.xmlsoap.org/soap/encoding/",
        },
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://schemas.xmlsoap.org/soap/encoding/",
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
