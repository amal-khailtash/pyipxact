from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


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
