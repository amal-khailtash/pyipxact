from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://schemas.xmlsoap.org/soap/encoding/"


@dataclass(slots=True)
class AnyType:
    class Meta:
        name = "anyType"
        namespace = "http://schemas.xmlsoap.org/soap/encoding/"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
