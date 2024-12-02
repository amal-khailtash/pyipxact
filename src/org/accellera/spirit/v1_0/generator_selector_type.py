from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1_0.group_selector import GroupSelector

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0"


@dataclass(slots=True)
class GeneratorSelectorType:
    class Meta:
        name = "generatorSelectorType"

    group_selector: Optional[GroupSelector] = field(
        default=None,
        metadata={
            "name": "groupSelector",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1.0",
            "required": True,
        },
    )
