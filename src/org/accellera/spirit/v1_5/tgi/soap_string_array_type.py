from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.5"


@dataclass(slots=True)
class SoapStringArrayType:
    class Meta:
        name = "soapStringArrayType"

    array_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "arrayType",
            "type": "Attribute",
            "namespace": "http://schemas.xmlsoap.org/soap/encoding/",
        },
    )