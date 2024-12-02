from dataclasses import dataclass, field
from typing import Optional

from org.accellera.spirit.v1685_2009.ve.pdp.group_selector import GroupSelector

__NAMESPACE__ = "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"


@dataclass(slots=True)
class GeneratorSelectorType:
    class Meta:
        name = "generatorSelectorType"

    group_selector: Optional[GroupSelector] = field(
        default=None,
        metadata={
            "name": "groupSelector",
            "type": "Element",
            "namespace": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009",
            "required": True,
        },
    )
