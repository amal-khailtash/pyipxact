from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class PersistentDataType:
    class Meta:
        name = "persistentDataType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
