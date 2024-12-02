from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.4"


@dataclass(slots=True)
class FloatArrayType:
    class Meta:
        name = "floatArrayType"

    array_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "arrayType",
            "type": "Attribute",
            "namespace": "http://schemas.xmlsoap.org/soap/encoding/",
        },
    )
