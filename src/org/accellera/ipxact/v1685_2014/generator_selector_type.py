from dataclasses import dataclass, field
from typing import Optional

from org.accellera.ipxact.v1685_2014.group_selector import GroupSelector

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2014"


@dataclass(slots=True)
class GeneratorSelectorType:
    class Meta:
        name = "generatorSelectorType"

    group_selector: Optional[GroupSelector] = field(
        default=None,
        metadata={
            "name": "groupSelector",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2014",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )